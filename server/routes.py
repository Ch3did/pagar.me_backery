from handlers.system_handlers import *
from handlers.backery_handlers import *

def load_routes(server):
    print(' * Loading Routes')
    app = server 
    app.secret_key = 'alura'

                                                            # System Routes
    #Home da API
    @app.route('/')
    def init():
        return home()

    #Methodo Ping pra teste de conexão
    @app.route('/ping', methods=['GET'])
    def ping():
        return handler_ping()

    #Cria a database para utilização da API
    @app.route('/create_db',methods=['GET'])
    def create_db():
        return handler_create_db()

                                                            #API Routes
    #Mostra todos os produtos cadastrados                                                        
    @app.route('/show_all_prod', methods=['GET'])
    def show_all():
        return handler_show_all()
    
    #Mostra os produtos filtrados por palavra-chave
    @app.route('/show_targuet',methods=['GET'])
    def show_one():
        return handler_show_one()

    #Cadastro de padarias    
    @app.route('/cad_backery',methods=['POST'])
    def new_backery():
        return handler_new_backery()

    #Login de padaria para cadastro ou exclusão de produtos
    @app.route('/login',methods=['POST'])
    def login():
        return handler_login()

    #Cadastro de novos produtos mediante Login
    @app.route('/cad_prod',methods=['POST'])
    def new_prod():
        return handler_new_backery()

    
    return app


