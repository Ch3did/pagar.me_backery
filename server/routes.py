import sys
sys.path.insert(1, './handlers')
from system_handlers import handler_ping

def load_routes(app):
    print(' * Loading Routes')
    @app.route('/', methods=['GET'])
    def home():
        return "<h1>Brioche Backery</h1><p>This site is a prototype API for register and transactions of products and bakeries.</p>"


    @app.route('/ping', methods=['GET'])
    def ping():
        return handler_ping()

    @app.route('/get_all_store',methods = ['GET'])
    def get_all_store():
        return handler_get_all_store()

    @app.route('/get_all_itens',methods = ['GET'])
    def get_all_itens():
        return handler_get_all_itens()    

    @app.route('/get_all_order',methods = ['GET'])
    def get_all_order():
        return handler_get_all_order()

    @app.route('/get_all_order_itens',methods = ['GET'])
    def get_all_order_itens():
        return handler_get_all_order_itens()


    app.run()


    return app


