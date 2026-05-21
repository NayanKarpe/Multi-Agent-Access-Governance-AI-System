import os

structure = [
    "app/routes",
    "app/services",
    "agents",
    "rag",
    "ml",
    "tools",
    "data/raw",
    "data/processed",
    "vectorstore",
    "orchestrator",
    "ui",
    "configs",
    "utils"
]

files = [
    "app/main.py",
    "agents/planner.py",
    "agents/auditor.py",
    "agents/risk.py",
    "agents/executor.py",
    "agents/memory.py",
    "rag/retriever.py",
    "ml/anomaly.py",
    "tools/db_tools.py",
    "orchestrator/graph.py",
    "ui/streamlit_app.py",
    "requirements.txt",
    "README.md"
]

for folder in structure:
    os.makedirs(folder, exist_ok=True)

for file in files:
    open(file, "w").close()

print("✅ Project structure created successfully!")
