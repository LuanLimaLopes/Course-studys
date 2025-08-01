#!/usr/local/bin/python3

from datetime import datetime

class projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    
    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self): #list comprehension
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
    
    def procurar(self, descricao):
        #possível index erro
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluída)' if self.feito else '')
    

def main():
    casa = projeto('Tarefas de casa')
    casa.add('Passar roupa')
    casa.add('Lavar prato')
    print(casa)

    casa.procurar('Passar roupa').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')

    corinthians = projeto('Elenco do corinthians')
    corinthians.add('Camisa 01: hugo souza')
    corinthians.add('Camisa 08: Rodrigo garro')
    corinthians.add('Camisa 10: Memphys depay')
    corinthians.add('Camisa 09: Yuri Alberto')


    for tarefa in corinthians:
        print(f'- {tarefa}')

if __name__ == '__main__':
    main()