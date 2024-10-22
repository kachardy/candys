from flask import Flask, render_template, request, flash, redirect 
import json

app = Flask('__name__')
app.config['SECRET_KEY'] = 'palavra-secreta123'

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/login')
def pagina_inicial():
    return render_template('login.html')

@app.route('/escolha')
def escolha():
    return render_template('escolha.html')

@app.route('/carrinhodecompra')
def carrinhodecompra():
    return render_template('carrinhodecompra.html')

@app.route('/loginf', methods = ['POST'])
def login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    with open('usuarios.json') as usuarios:
        lista = json.load(usuarios)
        cont = 0
        for c in lista:
            cont+=1
            if usuario == c["usuario"] and senha == c["senha"]:
                return render_template('produtos.html', nomeUsuario = c['usuario'])
            if cont >= len(lista):
                flash('Usuário inválido')
                return redirect('/login')
            
@app.route('/cadastrof', methods = ['POST'])
def cadastrar():
    user = []
    email = request.form.get('email')
    usuario = request.form.get('usuariocad')
    senha = request.form.get('senhacad')
    user = [{"email": email, "usuario": usuario,"senha": senha}]
    with open('usuarios.json') as usuarios:
        arquivo = json.load(usuarios)
        cont = 0
    arquivo2 = arquivo + user
    for c in arquivo:
        cont += 1
        if c["usuario"] != usuario and c["email"] != email:
            with open('usuarios.json', 'w') as arquivo:
                json.dump(arquivo2, arquivo, indent = 4)
            return render_template('login.html')
        if c["usuario"] == usuario or c["email"] == email:
            flash('Usuário já cadastrado')
            return redirect('/cadastro')
    
if __name__ == '__main__':    
    app.run(debug=True)