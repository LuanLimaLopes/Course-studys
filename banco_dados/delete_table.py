from pymysql.err import ProgrammingError
from db import nova_conexao

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute('DROP TABLE IF EXISTS emails')
        print('Tabela deletada!')
    except ProgrammingError as e:
        print(f'Erro: {e}')