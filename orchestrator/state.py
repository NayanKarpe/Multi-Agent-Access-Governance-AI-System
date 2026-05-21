from typing import TypedDict, List, Dict

class AgentState(TypedDict):
    query: str
    context: str
    plan: str
    audit: str
    risk: str
    anomalies: list
    scores: list