from rag.vector_store import VectorStore, save_index

def load_data():
    with open("data/raw/access_data.txt", "r") as f:
        docs = f.readlines()

    docs = [d.strip() for d in docs if d.strip()]

    store = VectorStore()
    store.build_index(docs)

    save_index(store)

    print("✅ FAISS index built and saved")


if __name__ == "__main__":
    load_data()