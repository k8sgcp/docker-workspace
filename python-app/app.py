import os
import datetime
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Container Node Status</title>
    <style>
        body { background-color: #0d1117; color: #58a6ff; font-family: monospace; padding: 2rem; }
        .card { border: 1px solid #30363d; border-radius: 6px; padding: 1.5rem; max-width: 500px; background: #161b22; }
        .status { color: #3fb950; font-weight: bold; }
        .label { color: #8b949e; }
    </style>
</head>
<body>
    <div class="card">
        <h2>> System Operational</h2>
        <p><span class="label">Container Host:</span> {{ hostname }}</p>
        <p><span class="label">Status:</span> <span class="status">ONLINE</span></p>
        <p><span class="label">Server Time:</span> {{ timestamp }}</p>
    </div>
</body>
</html>
"""


@app.route("/")
def dashboard():
    return render_template_string(
        HTML_TEMPLATE,
        hostname=os.uname().nodename,
        timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC"),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
