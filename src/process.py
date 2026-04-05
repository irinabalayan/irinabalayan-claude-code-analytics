import pandas as pd
import json


def extract_events(raw_batches):
    events = []

    for batch in raw_batches:
        for log in batch.get("logEvents", []):
            try:
                message = json.loads(log["message"])
                events.append(message)
            except:
                continue

    return events


def safe_int(x):
    try:
        return int(x)
    except:
        return None


def safe_float(x):
    try:
        return float(x)
    except:
        return None


def flatten_event(event):
    attrs = event.get("attributes", {})
    resource = event.get("resource", {})

    return {
        "timestamp": attrs.get("event.timestamp"),
        "event_type": event.get("body"),
        "event_name": attrs.get("event.name"),
        "session_id": attrs.get("session.id"),
        "user_id": attrs.get("user.id"),
        "user_email": attrs.get("user.email"),
        "model": attrs.get("model"),
        "input_tokens": safe_int(attrs.get("input_tokens")),
        "output_tokens": safe_int(attrs.get("output_tokens")),
        "cost_usd": safe_float(attrs.get("cost_usd")),
        "duration_ms": safe_int(attrs.get("duration_ms")),
        "tool_name": attrs.get("tool_name"),
        "tool_success": attrs.get("success"),
        "decision": attrs.get("decision"),
        "practice": resource.get("user.practice"),
    }


def build_dataframe(events):
    df = pd.DataFrame([flatten_event(e) for e in events])
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    return df


def clean_data(df):
    df = df.dropna(subset=["timestamp"])
    df = df.sort_values("timestamp")

    df["input_tokens"] = df["input_tokens"].fillna(0)
    df["output_tokens"] = df["output_tokens"].fillna(0)
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    return df