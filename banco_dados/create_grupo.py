from db import nova_conexao
from pymysql import ProgrammingError

create_table_grupo = """
    CREATE TABLE IF NOT EXISTS grupos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        descricao VARCHAR(30)
    )

"""

alter_table_contatos_1 = """
    ALTER TABLE contatos ADD grupo_id INT
"""

alter_table_contatos_2 = """
    ALTER TABLE contatos ADD FOREIGN KEY (grupo_id)
    REFERENCES grupos(id)
"""


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(create_table_grupo)
        cursor.execute(alter_table_contatos_1)
        cursor.execute(alter_table_contatos_2)
    except ProgrammingError as e:
        print(f'Erro: {e}')
    else:
        print('Tabela Criada!')
        print('Tabela Alterada!')
