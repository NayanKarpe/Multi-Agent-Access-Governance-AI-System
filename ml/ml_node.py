from ml.anomaly import detect_anomalies, calculate_risk_scores

def ml_node(state):
    context = state["context"]

    anomalies = detect_anomalies(context)

    return {"anomalies": anomalies}

def ml_node(state):
    context = state["context"]

    anomalies = detect_anomalies(context)
    scores = calculate_risk_scores(context)

    return {
        "anomalies": anomalies,
        "scores": scores
    }