from flask import jsonify, request, flash, redirect
from database.models import cadastro

# from testes.teste_db import teste_showall

def handler_show_all():
    # value = teste_showall()
    return json.dumps(value)

def handler_show_one():
    value = teste_showOne()
    return json.dumps(value)

def handler_new_backery():
    jsn = request.get_json()
    if jsn  == None:
        return "<h1>Faltaram alguns dados em sua requisição</h1>"
    else:
        cadastro(jsn)
        flash('Cadastro realizado com sucesso')
        return redirect('/')

def handler_delete():
    return "OK"