from db import nova_conexao
from pymysql import ProgrammingError, cursors

sql = """
    SELECT
        grupos.descricao AS grupo,
        contatos.nome AS nome
    FROM contatos
    INNER JOIN grupos ON contatos.grupo_id = grupos.id
    ORDER BY grupo, nome
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor(cursors.DictCursor)
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e}')
    else:
        for contato in contatos:
            print(f'{contato["grupo"]}: {contato["nome"]}')