import subprocess
import datetime
import os
import pytz  # pip install pytz
from flask import Flask, Response

app = Flask(__name__)

@app.route('/htop')
def htop():
    # 1. Your Full Name
    full_name = "Your Full Name Here"

    # 2. System Username
    try:
        username = os.getlogin()  # might fail in some containers
    except:
        username = os.environ.get("USER", "unknown-user")

    # 3. Server Time in IST
    ist_time = datetime.datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S %Z")

    # 4. 'top' command output
    #    We use top in batch mode (-b) with one iteration (-n 1).
    top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode(errors="ignore")

    # Build the HTML response
    html = f"""
    <h1>/htop Endpoint</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <pre>{top_output}</pre>
    """
    return Response(html, mimetype='text/html')

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
