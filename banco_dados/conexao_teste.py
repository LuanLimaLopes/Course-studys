from db import nova_conexao

with nova_conexao() as conexao:
    if conexao.open:
        print('Conectado!')
