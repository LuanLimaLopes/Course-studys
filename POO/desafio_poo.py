# Regras
# Ao converter cliente ou vendedor deve mostrar nome e idade
# metodo cliente.registra.compra() recebe um objeto compra
# metodo cliente.registra.compras() deve retornar um somatorio das compras
# metodo cliente.get_data_ultima_compra() deve retornar a data da ultima compra
# a propriedade compra.vendedor é do tipo vendedor
from datetime import datetime, timedelta

class Humano:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.pessoas = []
    
    def __iter__(self):
        return self.pessoa.__iter__()
    
    def __str__(self):
        return f'{self.nome} ({len(self.pessoa())} Pessoas na lista. '
    
    def pessoa(self): #list comprehension
        return [pessoas for pessoas in self.pessoa]

    def add(self, pessoa):
        self.pessoas.append(Humano(pessoa))

class vendedor(Humano):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)

    def salario(self,salario):
        self.salario = salario
    

class cliente(Humano):
    def __init__(self,nome,idade):
        super().__init__(nome, idade)

    def registrar_compra(self, compra):
        self.registrar_compra = compra
    
    def get_data_ultima_compra(self, compra, data):
        self.get_data = data
        self.compra = compra
    def total_compras(self, compras):
        self.compras = compras

class compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.compra = valor
   

def main():
    loja = Humano('cleber')
    loja.add('Lucas')
    print(loja)