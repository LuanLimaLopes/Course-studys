from db import nova_conexao
from pymysql.err import ProgrammingError

sql = 'Select * from contatos'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e}')
    else:
        for contato in contatos:
            print(f'{contato[2]:2d} - {contato[0]:20s} Telefone: {contato[1]}')