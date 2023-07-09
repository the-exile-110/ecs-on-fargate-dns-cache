from flask import Flask, render_template, request, jsonify
from datetime import datetime
import subprocess
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/get_delay", methods=["POST"])
def get_delay():
    domain = request.form.get("domain")
    output = subprocess.check_output("dig " + domain, shell=True).decode()
    delay = float(re.search(r"Query time: (\d+) msec", output).group(1)) / 1000
    current_time = datetime.now().strftime("%H:%M:%S")
    return jsonify({"delay": delay, "date": current_time})

if __name__ == "__main__":
    app.run(debug=True)