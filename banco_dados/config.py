from pymysql import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    password='12345678'
)

print('Conexão bem sucedida!')
conexao.close