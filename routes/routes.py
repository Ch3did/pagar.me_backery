from views.system_views import handler_ping


def load_routes(conn):
    print(' * Loading Routes')
    app = conn['app']
    engine  = conn['engine']
                                                         # System Routes
    #Home da API
    @app.route('/')
    def init():
        return "<h1>Index</h1>"

    #Ping pra teste de conexão
    @app.route('/ping', methods=['GET'])
    def ping():
        return handler_ping()

    #Cria a database para utilização da API
    @app.route('/create_db',methods=['GET'])
    def create_db():
        pass
        #return handler_create_db()

                                                            #API Routes
    #Mostra todos os produtos cadastrados                                                        
    @app.route('/show_all_prod', methods=['GET'])
    def show_all():
        pass
        #return handler_show_all()
    
    #Mostra os produtos filtrados por palavra-chave
    @app.route('/show_targuet',methods=['GET'])
    def show_one():
        pass
        #return handler_show_one()

    #Cadastro de padarias    
    @app.route('/cad_backery',methods=['POST'])
    def new_backery():
        pass
        #return handler_new_backery()

    #Login de padaria para cadastro ou exclusão de produtos
    @app.route('/login',methods=['POST'])
    def login():
        pass
        #return handler_login()

    #Cadastro de novos produtos mediante Login
    @app.route('/cad_prod',methods=['POST'])
    def new_prod():
        pass
        #return handler_new_backery()

    


