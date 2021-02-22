import flask
from flask import request, jsonify
import sqlite3
from routes import load_routes

def start_server():
  print(' * Starting Server')

  app = flask.Flask(__name__)
  app.config["DEBUG"] = True

  app = load_routes(app)

  app.run()