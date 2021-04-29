
from flask import jsonify

def handler_ping():
    return jsonify({'anwser':'pong'})