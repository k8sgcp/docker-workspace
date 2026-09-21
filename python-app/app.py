import os
import platform
import datetime
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Azure DevOps Health Dashboard</title>
    <style>
        body { background-color: #0f172a; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; padding: 2rem; }
        .card { border: 1px solid #334155; border-radius: 12px; padding: 1.5rem; max-width: 550px; background: #1e293b; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3); }
        h2 { color: #38bdf8; margin-top: 0; font-size: 1.5rem; }
        .row { display: flex; justify-content: space-between; border-bottom: 1px solid #334155; padding: 0.75rem 0; }
        .row:last-child { border-bottom: none; }
        .label { color: #94a3b8; font-weight: 500; }
        .value { font-weight: 600; }
        .badge { background-color: #059669; color: #ecfdf5; padding: 0.2rem 0.6rem; border-radius: 9999px; font-size: 0.85rem; }
    </style>
</head>
<body>
    <div class="card">
        <h2>🚀 Azure DevOps Target Node</h2>
        <div class="row">
            <span class="label">Status</span>
            <span class="value"><span class="badge">HEALTHY</span></span>
        </div>
        <div class="row">
            <span class="label">Container ID / Host</span>
            <span class="value" style="color: #f43f5e;">{{ hostname }}</span>
        </div>
        <div class="row">
            <span class="label">Environment</span>
            <span class="value">{{ env }}</span>
        </div>
        <div class="row">
            <span class="label">OS Architecture</span>
            <span class="value">{{ platform_info }}</span>
        </div>
        <div class="row">
            <span class="label">Last Deployment</span>
            <span class="value">{{ timestamp }}</span>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def dashboard():
    return render_template_string(
        HTML_TEMPLATE,
        hostname=os.uname().nodename,
        env=os.getenv("APP_ENV", "Staging-v2.0"),
        platform_info=f"{platform.system()} {platform.machine()}",
        timestamp=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
