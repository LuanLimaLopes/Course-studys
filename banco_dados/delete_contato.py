from db import nova_conexao
from pymysql import ProgrammingError


sql = "DELETE FROM contatos WHERE nome = %s "
args = ('lucas',)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro {e}')
    else:
        print(f'{cursor.rowcount} Registro(s) deletado(s).')