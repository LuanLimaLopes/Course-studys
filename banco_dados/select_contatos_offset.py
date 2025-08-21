from db import nova_conexao
from pymysql import ProgrammingError

sql = "SELECT * FROM contatos LIMIT %s OFFSET %s"
args = (2, 4)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e}')
    else:
        for contato in contatos:
            print(f'{contato[2]:2d} - {contato[0]:10s} TELEFONE {contato[1]}')