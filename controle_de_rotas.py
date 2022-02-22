from flask import Flask, jsonify, request, render_template
import bd_access

app = Flask(__name__)

# rendereiza a tela inicial
@app.route("/")
def home():
    return render_template('index.html')

# rendereriza a tela de cadastro
@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

# criar a rota de inserção de usuário novo
@app.route("/cadastrar", methods=["POST", "GET"])
def cadastrar_usuario():
    # meu código aqui
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    bd_access.insere_usuario(nome, email, senha)

    return render_template('index.html')


# criar a rota de listagem de usuários
@app.route("/usuarios")
def listar_usuarios():
    lista = bd_access.lista_usuarios()
    return render_template('lista_usuarios.html', lista=lista)


if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)
