from rag.retriever import retrieve_data

def retrieval_node(state):
    query = state["query"]

    context = retrieve_data(query)

    return {"context": context}