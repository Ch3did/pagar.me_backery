import flask
from routes.routes import load_routes
from database.conection import connection

def main(engine):
    print(' * System Starting') 
    app = flask.Flask(__name__)
    load_routes(app)
    app.run(debug=True)


if __name__ == "__main__":
    main(connection())