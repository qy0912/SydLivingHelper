from fastapi import FastAPI
from pydantic import BaseModel
import os

# 如果希望从项目根目录的 .env 文件读取 OPENAI_API_KEY，请安装 python-dotenv：
#   pip install python-dotenv
from dotenv import load_dotenv

from app.rag.embeddings import EmbeddingGenerator
from app.rag.vector_store import VectorStore
from app.rag.retriever import Retriever
from app.rag.generator import AnswerGenerator

from fastapi.middleware.cors import CORSMiddleware


# -----------------------------
# FastAPI App Initialization
# -----------------------------
app = FastAPI(
    title="Sydney Housing Assistant",
    description="A RAG-based assistant for Sydney suburbs, rentals, and property knowledge.",
    version="1.0.0"
)

# Allow local frontend or tools to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Load API Key
# -----------------------------
# 从项目根目录的 .env 文件加载环境变量（如果你在 .env 里设置了 OPENAI_API_KEY）
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY not found. Please set it as an environment variable.")


# -----------------------------
# Initialize RAG Components
# -----------------------------
EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4o-mini"
INDEX_PATH = "models/faiss_index.bin"

# Embedding generator
embedder = EmbeddingGenerator(api_key=API_KEY, model=EMBEDDING_MODEL)

# Vector store
vector_store = VectorStore(dim=1536, index_path=INDEX_PATH)
vector_store.load()

# Retriever
retriever = Retriever(vector_store=vector_store, embedder=embedder)

# Answer generator
generator = AnswerGenerator(api_key=API_KEY, model=LLM_MODEL)


# -----------------------------
# Request Schema
# -----------------------------
class QueryRequest(BaseModel):
    query: str
    top_k: int = 5


# -----------------------------
# API Endpoint
# -----------------------------
@app.post("/ask")
def ask_question(payload: QueryRequest):
    query = payload.query
    top_k = payload.top_k

    # Retrieve relevant chunks
    chunks = retriever.retrieve(query, top_k=top_k)

    # Generate answer
    answer = generator.generate(query, chunks)

    return {
        "query": query,
        "chunks_used": chunks,
        "answer": answer
    }


# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def root():
    return {"message": "Sydney Housing Assistant API is running."}
