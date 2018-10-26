from app.blueprints import main
from flask import request
from flask import jsonify


@main.route("/", methods=['GET'])
def home():
    data = {
        "count": 1,
        "data": "Welcome to Flask"
    }

    return jsonify(data)
