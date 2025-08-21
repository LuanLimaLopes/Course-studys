from db import nova_conexao

sql = 'SELECT nome, tel FROM contatos'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    print(cursor.fetchone())

     #for x in cursor.fetchall():
       # print(x)