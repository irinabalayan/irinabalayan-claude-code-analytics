# platform/src/analyze.py
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest

# ---------- Analytics functions ----------

def token_usage_by_role(df):
    return df.groupby("practice")[["input_tokens", "output_tokens"]].sum()

def peak_usage_hours(df):
    df["hour"] = df["timestamp"].dt.hour
    return df.groupby("hour").size()

def tokens_over_time(df):
    return df.groupby(df["timestamp"].dt.date)[["input_tokens", "output_tokens"]].sum()

def top_models(df):
    return df["model"].value_counts().head(10)

def avg_session_tokens(df):
    return df.groupby("session_id")[["input_tokens", "output_tokens"]].sum().mean()

def session_length(df):
    return df.groupby("session_id")["duration_ms"].sum()

def cost_by_role(df):
    return df.groupby("practice")["cost_usd"].sum()


# ---------- Prediction ----------

def predict_token_trend(df, days_ahead=7):
    """
    Predict future total_tokens using Linear Regression.
    Returns:
        daily: DataFrame with historical totals
        future_df: DataFrame with future predictions
    """
    # Ensure total_tokens exists
    if "total_tokens" not in df.columns:
        df["total_tokens"] = df["input_tokens"] + df["output_tokens"]

    # Aggregate by day
    daily = df.groupby(df["timestamp"].dt.date)["total_tokens"].sum().reset_index()
    daily["timestamp"] = pd.to_datetime(daily["timestamp"])

    # Prepare regression
    daily["date_ordinal"] = daily["timestamp"].map(lambda x: x.toordinal())
    X = daily[["date_ordinal"]]
    y = daily["total_tokens"]

    model = LinearRegression()
    model.fit(X, y)

    # Predict future dates
    future_ordinals = np.arange(X["date_ordinal"].max() + 1, X["date_ordinal"].max() + 1 + days_ahead)
    future_preds = model.predict(future_ordinals.reshape(-1, 1))

    future_df = pd.DataFrame({
        "date": [pd.Timestamp.fromordinal(int(d)) for d in future_ordinals],
        "predicted_tokens": future_preds
    })

    return daily, future_df


# ---------- Anomaly detection ----------

def detect_anomalies(df, contamination=0.05):
    """
    Detect anomalies in total_tokens using IsolationForest.
    Adds a new column 'anomaly' to df:
        1 : normal
       -1 : anomaly
    """
    if "total_tokens" not in df.columns:
        df["total_tokens"] = df["input_tokens"] + df["output_tokens"]

    model = IsolationForest(contamination=contamination, random_state=42)
    df["anomaly"] = model.fit_predict(df[["total_tokens"]])

    anomalies = df[df["anomaly"] == -1]
    print(f"Detected {len(anomalies)} anomalies out of {len(df)} events")

    return df