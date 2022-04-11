from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.sql.expression import true

engine = create_engine('sqlite:///ads4a.db')

# criando a tabela de usuários
with engine.connect() as con:
    create_alunos = """
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            endereco TEXT NOT NULL
        )
    """

    rs = con.execute(create_alunos)

# criar função para inserir um usuário
def insere_aluno(nome, email, endereco):
    # é interessante validar os dados antes de inserir
    # é interessante validar se usuário já existe antes de inserir
    with engine.connect() as con:
        statement = text("""
            INSERT INTO alunos VALUES (:id, :nome, :email, :endereco)
        """)
        con.execute(statement, id=None, nome=nome, email=email, endereco=endereco)

# criar função para listar usuários
def lista_alunos():
    with engine.connect() as con:
        statement = text("""
            SELECT nome, email FROM alunos
        """)
        rs = con.execute(statement)
        lista_de_alunos = []
        while True:
            aluno = rs.fetchone()
            if aluno == None:
                break
            lista_de_alunos.append(aluno)
        return lista_de_alunos


if __name__ == '__main__':
    insere_aluno("Anedino", "dino@dino","1234")
    lista = lista_alunos()
    print(lista)
