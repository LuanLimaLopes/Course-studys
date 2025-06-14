
arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close

for registros in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registros.split(',')))
    