from langgraph.graph import StateGraph
from orchestrator.state import AgentState

from agents.planner import planner_node
from agents.auditor import auditor_node
from agents.risk import risk_node
from rag.retrieval_node import retrieval_node
from ml.ml_node import ml_node


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_node)
    graph.add_node("retrieval", retrieval_node)
    graph.add_node("ml", ml_node)  # ✅ NEW
    graph.add_node("auditor", auditor_node)
    graph.add_node("risk", risk_node)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "retrieval")
    graph.add_edge("retrieval", "ml")      # ✅ NEW
    graph.add_edge("ml", "auditor")        # ✅ NEW
    graph.add_edge("auditor", "risk")

    graph.set_finish_point("risk")

    return graph.compile()


graph = build_graph()

def run_pipeline(user_query):
    result = graph.invoke({"query": user_query})

    return f"""
=== PLAN ===
{result.get("plan")}

=== CONTEXT ===
{result.get("context")}

=== ML ANOMALIES ===
{result.get("anomalies")}

=== RISK SCORES ===
{result.get("scores")}

=== AUDIT ===
{result.get("audit")}

=== RISK ===
{result.get("risk")}
"""
