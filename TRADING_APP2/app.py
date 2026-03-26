from flask import Flask, render_template
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
    data = load_status()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)