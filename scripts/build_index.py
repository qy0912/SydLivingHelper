import os
import sys

# 让脚本可以找到 app/ 目录
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# 如果你希望从项目根目录的 .env 文件加载环境变量，请安装 python-dotenv:
#   pip install python-dotenv
from dotenv import load_dotenv

from app.rag.loader import DocumentLoader
from app.rag.chunker import TextChunker
from app.rag.embeddings import EmbeddingGenerator
from app.rag.vector_store import VectorStore


# 从根目录加载 .env（默认会查找当前工作目录下的 .env）
load_dotenv()

DATA_DIR = "data"                     # 你的知识库目录
INDEX_PATH = "models/faiss_index.bin" # 保存向量库的位置
EMBEDDING_MODEL = "text-embedding-3-small"
API_KEY = os.getenv("OPENAI_API_KEY")  # 从环境变量读取 API key


def build_index():
    print("📥 Loading documents...")
    loader = DocumentLoader(DATA_DIR)
    documents = loader.load_all_documents()

    print(f"Loaded {len(documents)} documents.")

    print("✂️ Chunking documents...")
    chunker = TextChunker(chunk_size=300, overlap=50)

    all_chunks = []
    for doc in documents:
        chunks = chunker.chunk_text(doc["text"])
        all_chunks.extend(chunks)

    print(f"Generated {len(all_chunks)} chunks.")

    print("🧬 Generating embeddings...")
    embedder = EmbeddingGenerator(api_key=API_KEY, model=EMBEDDING_MODEL)
    embeddings = embedder.embed(all_chunks)

    print("📦 Building FAISS index...")
    dim = len(embeddings[0])  # embedding 维度
    vector_store = VectorStore(dim=dim, index_path=INDEX_PATH)
    vector_store.add_embeddings(embeddings, all_chunks)

    print("💾 Saving index...")
    vector_store.save()

    print("✅ Index build complete!")
    print(f"Saved to: {INDEX_PATH}")


if __name__ == "__main__":
    build_index()
