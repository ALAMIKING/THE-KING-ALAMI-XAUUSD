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
    except Exception as e:
        print("LOAD ERROR:", e)
        return {}

def save_status(data):
    try:
        with open(STATUS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        print("SAVE ERROR:", e)
        return False

@app.route("/")
def home(): 
    data = load_status()
    return render_template("index.html", data=data)

@app.route("/status")
def status():
    return jsonify(load_status())

@app.route("/update_status", methods=["POST"])
def update_status():
    data = request.get_json()

    if not data:
        return jsonify({"success": False, "error": "No data received"}), 400

    ok = save_status(data)

    if ok:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "error": "Save failed"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
