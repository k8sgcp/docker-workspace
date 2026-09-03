import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("POSTGRES_DB", "appdb"),
        user=os.environ.get("POSTGRES_USER", "appuser"),
        password=os.environ.get("POSTGRES_PASSWORD", "appsecret")
    )
    return conn

@app.route("/api/data")
def get_data():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT VERSION();")
        db_version = cur.fetchone()[0]
        cur.close()
        conn.close()
        return jsonify({"status": "success", "db_version": db_version})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
