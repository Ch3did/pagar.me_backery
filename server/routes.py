from flask import Flask, render_template, jasonify
import bcrypt

app = Flask('__name__')

@app.route('/')
def index():
    return render_template('index.html', titulo = "Início")


@app.route('/cadastro')
def cadastro():
    return jasonify("{'result': 'success'}")


@app.route('/pagamento')
def pagamento():
    return 'pagamento'


# @app.router('/login')
# def login():
#     pass
@app.route('/autenticar')
def autenticar():
    if 'mestra'==request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] +'logou com sucesso')
        return redirect('/')
    else:
        flash('Não logado, tente novamente')
        return redirect('/login')


@app.route('/compra')
def compra():
    return 'compra'


app.run(debug=True)



