import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Chikoo Music Bot is Running!"

def run():
    port = int(os.environ.get("PORT", 10000))
    print(f"Starting Flask on port {port}")
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
        use_reloader=False,
    )
