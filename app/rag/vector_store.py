import faiss
import numpy as np
import pickle
import os

class VectorStore:
    def __init__(self, dim: int, index_path="models/faiss_index.bin"):
        self.dim = dim
        self.index_path = index_path
        self.index = faiss.IndexFlatL2(dim)
        self.text_chunks = []

    def add_embeddings(self, embeddings, chunks):
        self.text_chunks.extend(chunks)
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)

    def save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.index_path + ".meta", "wb") as f:
            pickle.dump(self.text_chunks, f)

    def load(self):
        if not os.path.exists(self.index_path):
            raise FileNotFoundError("FAISS index not found.")
        self.index = faiss.read_index(self.index_path)
        with open(self.index_path + ".meta", "rb") as f:
            self.text_chunks = pickle.load(f)

    def search(self, query_embedding, top_k=5):
        query_vector = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query_vector, top_k)
        results = [self.text_chunks[i] for i in indices[0]]
        return results
