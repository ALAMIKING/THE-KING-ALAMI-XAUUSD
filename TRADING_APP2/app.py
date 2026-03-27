from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

STATUS_FILE = "bot_status.json"

def load_status():
    if not os.path.exists(STATUS_FILE):
        return {}

    try:
        with open(STATUS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/status")
def status():
    return jsonify(load_status())

@app.route("/update_status", methods=["POST"])
def update_status():
    try:
        data = request.json
        with open(STATUS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return {"success": True, "message": "Status updated"}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
