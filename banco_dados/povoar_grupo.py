from db import nova_conexao
from pymysql import ProgrammingError

sql = "INSERT INTO grupos (descricao) VALUES (%s) "
args = (
    ('Familia'),
    ('Futebol'),
    ('Igreja'),
    ('Trabalho')
)


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e}')
    else:
        print(f'{cursor.rowcount} Registro(s) inserido(s).')