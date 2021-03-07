import flask
from server.routes import load_routes
from database import connection

def start_server(config):
  print(' * Starting Server')
  
  server = {
    'app': flask.Flask(__name__),
    'db': connection.get_connection(config["db"])
  }
  server["app"].config["DEBUG"] = True

  server = load_routes(server)

  server["app"].run()