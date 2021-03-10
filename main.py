import flask
from server.routes import load_routes

def main():
    print(' * System Starting') 
  
    app = flask.Flask(__name__)

    app.config["DEBUG"] = True

    load_routes(app)

    app.run()


main()