import sys
sys.path.insert(1, './handlers')
from system_handlers import handler_ping

def load_routes(app):
    print(' * Loading Routes')
    @app.route('/ping', methods=['GET'])
    def ping():
        return handler_ping()

    return app