from handlers.system_handlers import *
from handlers.store_handlers import *

def load_routes(server):
    print(' * Loading Routes')
    app = server["app"]

    # System Routes
    @app.route('/ping', methods=['GET'])
    def ping():
        return handler_ping()


    

    server["app"] = app

    return server


