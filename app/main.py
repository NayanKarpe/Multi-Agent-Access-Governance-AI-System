from fastapi import FastAPI
from orchestrator.graph import run_pipeline

app = FastAPI()

@app.get("/query")
def query(q: str):
    result = run_pipeline(q)

    print("FINAL RESULT:", result)

    return {"response": result}