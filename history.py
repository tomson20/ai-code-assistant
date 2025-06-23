import json
import requests
from datetime import datetime

GIST_ID = "YOUR_GITHUB_GIST_ID"
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def load_history():
    response = requests.get(f"https://api.github.com/gists/{GIST_ID}") 
    if response.status_code == 200:
        content = response.json()['files']['history.json']['content']
        return json.loads(content)
    return []

def save_history(history):
    payload = {
        "files": {
            "history.json": {
                "content": json.dumps(history, indent=4)
            }
        }
    }
    requests.patch(f"https://api.github.com/gists/{GIST_ID}",  headers=HEADERS, json=payload)

def log_task(task, code, tests="", docs=""):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "task": task,
        "code": code,
        "tests": tests,
        "docs": docs
    }

    history = load_history()
    history.append(entry)
    save_history(history)

def get_history():
    return load_history()