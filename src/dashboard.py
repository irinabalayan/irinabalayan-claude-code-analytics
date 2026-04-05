# platform/src/dashboard.py
import streamlit as st
import pandas as pd
from src.analyze import *
import matplotlib.pyplot as plt

def run_dashboard(df):
    st.title("Claude Code Analytics Dashboard")

    # Ensure total_tokens exists
    if "total_tokens" not in df.columns:
        df["total_tokens"] = df["input_tokens"] + df["output_tokens"]

    # ---------- Basic insights ----------
    st.subheader("Token Usage Over Time")
    st.line_chart(tokens_over_time(df))

    st.subheader("Token Usage by Role")
    st.bar_chart(token_usage_by_role(df))

    st.subheader("Peak Usage Hours")
    st.bar_chart(peak_usage_hours(df))

    st.subheader("Top Models")
    st.bar_chart(top_models(df))

    st.subheader("Tool Usage")
    st.bar_chart(df["tool_name"].value_counts())

    st.subheader("Session Length (Total Duration per Session)")
    st.bar_chart(session_length(df))

    st.subheader("Cost by Role")
    st.bar_chart(cost_by_role(df))

    # ---------- Anomalies ----------
    st.subheader("Anomalies in Token Usage")
    df = detect_anomalies(df)

    # ---------- Token Usage Trend with Prediction and Anomalies ----------
    st.subheader("Token Usage Trend with Prediction and Anomalies")

    # Aggregate numeric daily totals
    daily = df.groupby(df["timestamp"].dt.date)[["input_tokens", "output_tokens", "total_tokens"]].sum().reset_index()
    daily["timestamp"] = pd.to_datetime(daily["timestamp"])

    # Aggregate anomalies per day
    daily_anomalies = df[df["anomaly"] == -1].groupby(df["timestamp"].dt.date)[["total_tokens"]].sum().reset_index()
    daily_anomalies["timestamp"] = pd.to_datetime(daily_anomalies["timestamp"])

    # Predict future tokens
    _, future = predict_token_trend(df)

    plt.figure(figsize=(12,6))

    # Actual tokens
    plt.plot(daily["timestamp"], daily["total_tokens"], label="Actual Tokens", color="blue")

    # Predicted tokens
    plt.plot(future["date"], future["predicted_tokens"], linestyle="--", color="green", label="Predicted Tokens")

    # Anomalies
    plt.scatter(daily_anomalies["timestamp"], daily_anomalies["total_tokens"], color="red", label="Anomalies", s=50)

    plt.xlabel("Date")
    plt.ylabel("Total Tokens")
    plt.title("Token Usage Trend with Prediction and Anomalies")
    plt.legend()
    plt.tight_layout()
    st.pyplot(plt)