from src.ingest import load_data
from src.process import extract_events, build_dataframe, clean_data
from src.database import save_to_db
from src.dashboard import run_dashboard
from src.analyze import detect_anomalies
import streamlit as st
import os


def main():
    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    # Load raw telemetry data
    raw = load_data("data/raw/telemetry_logs.jsonl")
    print(f"Loaded {len(raw)} raw events")

    # Extract and process events
    events = extract_events(raw)
    df = build_dataframe(events)
    df = clean_data(df)
    print(f"Processed {len(df)} events into clean dataframe")

    # Detect anomalies
    df = detect_anomalies(df)
    df.to_csv("output/anomaly_detection.csv", index=False)
    print("Saved anomaly detection results to output/anomaly_detection.csv")

    # Save to database
    save_to_db(df)
    print("Saved dataframe to database")

    # Run Streamlit dashboard
    run_dashboard(df)


if __name__ == "__main__":
    main()