from database.models import model
from flask import jsonify, flash, redirect


def home():
  return '<h1>API FLASK</h1>'



def handler_ping():
      return jsonify({
    'result': 'pong'
  })



def handler_create_db():
  model()
  return redirect ('/')