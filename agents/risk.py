from app.services.llm import query_llama


def risk_node(state):
    audit_result = state["audit"]
    prompt = f"""
You are a Risk Analysis Expert.

AUDIT RESULT:
{audit_result}

TASK:
- Give BUSINESS IMPACT in short bullet points
- Keep each point concise
- Focus on real risks

OUTPUT FORMAT:

User: <name>
- Risk Impact: ...
- Security Concern: ...
- Recommended Action: ...
"""
    
    risk = query_llama(prompt)

    return {"risk": risk}
