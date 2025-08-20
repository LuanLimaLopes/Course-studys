from db import nova_conexao
from pymysql.err import ProgrammingError

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Ana', '18765-4321'),
    ('Bia', '28765-4321'),          
    ('Luca', '38765-4321'),  
    ('Lavinia', '48765-4321'),  
    ('Luan', '58765-4321'),  
    ('Pedro', '68765-4321'),  
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e}')
    else:
        print(f'Foram incluídos {cursor.rowcount} Registros!')