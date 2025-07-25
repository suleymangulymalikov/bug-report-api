from flask import request, Flask
from uuid import uuid4
from datetime import datetime

from db import bug_reports

app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Welcome to Bug Report API"}


@app.route("/bug-reports", methods=["GET"])
def get_all_bug_reports():
    return bug_reports


@app.route("/bug-report", methods=["POST"])
def create_bug_report():
    data = request.get_json()
    required_fields = ["user_name", "bug_title", "bug_description", "bug_severity"]

    for field in required_fields:
        if field not in data:
            return {"error": f"Missing field: {field}"}, 400

    if data["bug_severity"] not in ["low", "medium", "high"]:
        return {"error": "Severity must be low, medium, or high"}

    if not data:
        return {"message": "Empty respond"}

    bug_report = {
        "user_id": uuid4().hex,
        "user_name": data["user_name"],
        "bug_title": data["bug_title"],
        "bug_description": data["bug_description"],
        "bug_severity": data["bug_severity"],
        "timestamp": datetime.now(),
    }
    bug_reports.append(bug_report)
    return bug_report, 201


@app.route("/bug-report/<user_id>", methods=["GET"])
def get_bug_report_by_user_id(user_id):
    for bug_report in bug_reports:
        if bug_report["user_id"] == user_id:

            return bug_report
    return {"message": "Bug report not found"}, 404


@app.route("/bug-report/<user_id>", methods=["DELETE"])
def delete_bug_report_by_user_id(user_id):
    for bug_report in bug_reports:
        if bug_report["user_id"] == user_id:
            bug_reports.remove(bug_report)
            return bug_report
    return {"message": "Bug report not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)
