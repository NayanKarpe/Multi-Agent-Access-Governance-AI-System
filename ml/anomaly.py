import pandas as pd
from sklearn.ensemble import IsolationForest

# Convert text → structured features
def parse_data_to_df(text_data):
    rows = []

    for line in text_data.split("\n"):
        if "User" in line:
            user = line.split("has")[0].strip()

            role_score = 0
            app_count = 1

            if "Admin" in line:
                role_score += 2
            if "Developer" in line:
                role_score += 3
            if "Viewer" in line or "Read" in line:
                role_score += 1

            if "and" in line:
                app_count = 2

            rows.append({
                "user": user,
                "role_score": role_score,
                "app_count": app_count
            })

    return pd.DataFrame(rows)



def detect_anomalies(text_data):
    df = parse_data_to_df(text_data)

    if df.empty:
        return "No valid data for ML analysis"

    # ML prediction
    model = IsolationForest(contamination=0.3, random_state=42)
    df["anomaly"] = model.fit_predict(df[["role_score", "app_count"]])

    # ✅ RULE-BASED OVERRIDE
    def apply_rules(row):
        # Force anomaly if Admin + Developer (highly critical)
        if row["role_score"] >= 5:   # Admin (2) + Developer (3) = 5
            return -1
        return row["anomaly"]

    df["anomaly"] = df.apply(apply_rules, axis=1)

    # Return only anomalies
    anomalies = df[df["anomaly"] == -1]

    return anomalies.to_dict(orient="records")

def calculate_risk_scores(text_data):
    df = parse_data_to_df(text_data)

    if df.empty:
        return []

    df["risk_score"] = (
        df["role_score"] * 2
        + df["app_count"]
    )

    return df.to_dict(orient="records")
