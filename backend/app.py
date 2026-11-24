from flask import Flask, jsonify, send_from_directory
from pathlib import Path
from flask_cors import CORS

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app = Flask(__name__, static_folder=str(FRONTEND_DIR), static_url_path="/static")
CORS(app)

@app.get("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.get("/api/hello")
def hello():
    return jsonify(message="Hello from Flask!")


if __name__ == "__main__":
    app.run(debug=True)