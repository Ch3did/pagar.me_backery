from flask import jsonify
from testes.teste_db import teste_showall

def handler_show_stores(db_connection):
    value = teste_showall()
    return jsonify({
        
    })
