from .pessoa import Pessoa
# ponto importa de forma relativa

def get_date(compra):
    return compra.data

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compra(self, compra):
        self.compras.append(compra)

    def get_date_ultima_compra(self):
        return None if not self.compras else \
            sorted(self.compras, key=get_date)[-1].data
    
    def total_compras(self):
        total = 0
        for compra in self.compras:
            total += compra.valor
        return total
