import sqlite3
import pandas as pd

def save_to_db(df, db_path="db/database.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("events", conn, if_exists="replace", index=False)
    conn.close()


def load_from_db(db_path="db/database.db"):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM events", conn)
    conn.close()
    return df