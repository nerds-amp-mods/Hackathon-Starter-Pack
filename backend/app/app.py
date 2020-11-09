from typing import Any, Dict, Tuple

from flask import Flask

app = Flask(__name__)


@app.route("/")
def status() -> Tuple[Dict[str, Any], int]:
    return {"response": "Welcome to Landing Page"}, 200
