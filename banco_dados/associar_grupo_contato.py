from pymysql import ProgrammingError
from db import nova_conexao

sql = " SELECT id FROM grupos WHERE descricao = %s"
update = " UPDATE contatos SET grupo_id = %s WHERE nome = %s "

contato_grupo = {
    'Ana carolina': 'Familia',
    'Luan': 'Familia',
    'Bia': 'Igreja',
    'Luca': 'Trabalho',
    'Lavinia': 'Familia',
    'Pedro': 'Futebol',
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in contato_grupo.items():
            cursor.execute(sql, (grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(update, (grupo_id, contato))
            conexao.commit()
        
    except ProgrammingError as e:
        print(f'Erro: {e}')
    else:
        print('contatos associados!')