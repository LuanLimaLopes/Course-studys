#!/usr/local/bin/python3

from datetime import datetime, timedelta

class projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    
    #Funções privadas
    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)
    #Funções privadas
    #overloadings de funções
    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if  isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)


    def pendentes(self): #list comprehension
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
    
    def procurar(self, descricao):
        #possível index erro
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'

class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(concluída!)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')
        
        return f'{self.descricao} ' + ' '.join(status)
    

class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        #herança
        super().__init__(descricao,vencimento)
        self.dias = dias

    def concluir(self):
        #herança
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    casa = projeto('Tarefas de casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato', datetime.now() + timedelta(days=3, minutes=12))
    
    casa.add(TarefaRecorrente('Trocar lençois', datetime.now(), 7 ))
    casa.add(casa.procurar('Trocar lençois').concluir())

    print(casa)
    for tarefa in casa:
        print(f'- {tarefa}')

if __name__ == '__main__':
    main()