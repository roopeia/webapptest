from flask import Flask, jsonify, send_from_directory
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app = Flask(__name__, static_folder=str(FRONTEND_DIR), static_url_path="/static")


@app.get("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.get("/api/hello")
def hello():
    return jsonify(message="Hello from your Flask backend!")


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
