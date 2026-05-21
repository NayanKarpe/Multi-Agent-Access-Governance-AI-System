from app.services.llm import query_llama

def auditor_node(state):
    user_query = state["query"]
    data_context = state["context"]
    anomalies = state.get("anomalies", [])

    prompt = f"""
You are a strict Access Governance Auditor.

You are given REAL DATA below. You MUST ONLY use this data.

DO NOT:
- Ask for more data
- Say data is insufficient
- Explain methodology
- Assume anything outside given data

RISK RULES:
- Admin ONLY = HIGH RISK
- Admin + Developer = CRITICAL RISK
- Multiple apps = MEDIUM RISK
- Viewer/Read-only = LOW RISK

IMPORTANT:
- Admin only = HIGH (NOT CRITICAL)
- CRITICAL ONLY if Admin + Developer

DATA:
{data_context}

ML DETECTED ANOMALIES:
{anomalies}

QUESTION:
{user_query}

TASK:
- Identify users with HIGH or CRITICAL risk ONLY
- Give higher priority to ML-flagged anomalies
- Ignore LOW risk users
- Base everything ONLY on the data above

OUTPUT (STRICT FORMAT):
User: <name>
Risk: <level>
Reason: <short reason>

Do NOT output anything else.

RULES:
- Only explain risks based on user roles and access
- DO NOT discuss ML systems or technical internals
- Focus only on business/security impact
"""
    
    audit = query_llama(prompt)

    return {"audit": audit}
