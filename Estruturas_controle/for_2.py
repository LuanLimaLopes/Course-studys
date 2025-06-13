letras = 'corinthians'
for palavra in letras:
    print(palavra, end=' ')
print("Meu timão!")
print("campeão!")

#Percorrendo por uma lista
aprovados = ['cacá', 'andré ramalho', 'romero', 'yuri alberto']
for jogador in aprovados:
    print(jogador)

for posicao, jogador in enumerate(aprovados):
    print(f"{posicao + 1}", jogador)

#Percorrendo por uma tupla
dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta','Quinta','Sexta', 'sábado')

for dias in dias_semana:
    print(dias)