from db import nova_conexao
from pymysql import ProgrammingError


sql="UPDATE contatos SET nome = %s WHERE id = %s "
args = ('Ana carolina', 2)


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e}')
    else:
        print(f'{cursor.rowcount} - Registro(s) Atualizado(s).')