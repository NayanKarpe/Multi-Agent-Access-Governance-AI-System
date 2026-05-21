from app.services.llm import query_llama


def planner_node(state):
    user_query = state["query"]

    prompt = f"""
You are a task planner for an Access Governance AI system.

You already have:
- access data
- retrieval system
- auditing rules

USER QUERY:
{user_query}

TASK:
Break into actionable system steps only.

OUTPUT:
Step 1: Retrieve relevant access data
Step 2: Identify risky users based on roles
Step 3: Analyze business risk
"""
    
    plan = query_llama(prompt)

    return {"plan": plan}