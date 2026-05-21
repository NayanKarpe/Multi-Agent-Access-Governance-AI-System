from rag.vector_store import load_index

# Load once
try:
    vector_store = load_index()
    print("✅ Vector store loaded successfully")
except Exception as e:
    vector_store = None
    print(f"❌ Failed to load vector store: {e}")


def retrieve_data(query):
    if vector_store is None:
        return "No data available (vector store not loaded)"

    try:
        results = vector_store.search(query, k=3)

        if not results:
            return "No relevant data found"

        return "\n".join(results)

    except Exception as e:
        return f"Error retrieving data: {str(e)}"