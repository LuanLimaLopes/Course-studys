#!/usr/local/bin/python3

class SimpleClass:
    contador = 0
    
    def __init__(self):
        self.contar()
    
    @classmethod
    def contar(cls):
        cls.contador += 1

    

if __name__ == "__main__":
    list = [SimpleClass(), SimpleClass()]
    print(SimpleClass.contador) #Resultado esperado 2