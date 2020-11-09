from typing import Any, Dict, Tuple

from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome_route() -> Tuple[Dict[str, Any], int]:
    return {"response": "Welcome to Landing Page"}, 200
