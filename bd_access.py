from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.sql.expression import true

engine = create_engine('sqlite:///ads4a.db')

# criando a tabela de usuários
with engine.connect() as con:
    create_usuarios = """
        CREATE TABLE IF NOT EXISTS Usuarios (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    """

    rs = con.execute(create_usuarios)

# criar função para inserir um usuário
def insere_usuario(nome, email, senha):
    # é interessante validar os dados antes de inserir
    # é interessante validar se usuário já existe antes de inserir
    with engine.connect() as con:
        statement = text("""
            INSERT INTO Usuarios VALUES (:id, :nome, :email, :senha)
        """)
        con.execute(statement, id=None, nome=nome, email=email, senha=senha)

# criar função para listar usuários
def lista_usuarios():
    with engine.connect() as con:
        statement = text("""
            SELECT nome, email FROM Usuarios
        """)
        rs = con.execute(statement)
        lista_de_usuarios = []
        while True:
            usuario = rs.fetchone()
            if usuario == None:
                break
            lista_de_usuarios.append(usuario)
        return lista_de_usuarios


if __name__ == '__main__':
    insere_usuario("Anedino", "dino@dino","1234")
    lista = lista_usuarios()
    print(lista)
