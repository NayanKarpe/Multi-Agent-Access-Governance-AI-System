import faiss
import numpy as np
from rag.embeddings import get_embedding
import pickle
import json

class VectorStore:
    def __init__(self):
        self.texts = []
        self.index = None

    def build_index(self, documents):
        self.texts = documents
        
        embeddings = get_embedding(documents)

        if len(embeddings.shape) == 1:
            embeddings = embeddings.reshape(1, -1)

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

    def search(self, query, k=3):
        if self.index is None:
            raise ValueError("FAISS index not initialized")

        query_embedding = get_embedding(query)

        # ✅ FIX HERE
        if len(query_embedding.shape) == 1:
            query_embedding = query_embedding.reshape(1, -1)

        distances, indices = self.index.search(query_embedding, k)

        results = [
            self.texts[i]
            for i in indices[0]
            if i < len(self.texts)
        ]

        return results

def save_index(store):
    faiss.write_index(store.index, "vectorstore/faiss.index")

    with open("vectorstore/texts.json", "w") as f:
        json.dump(store.texts, f)


def load_index():
    store = VectorStore()

    store.index = faiss.read_index("vectorstore/faiss.index")

    with open("vectorstore/texts.json", "r") as f:
        store.texts = json.load(f)

    return store

# Global instance (simple for now)
vector_store = VectorStore()
