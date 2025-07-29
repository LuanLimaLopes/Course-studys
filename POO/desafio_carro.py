class Carro:
    def tipo(self):
        return f'Modelo: {self.modelo}, Marca:{self.marca},TopSpeed: {self.topSpeed}KM'
    
    def acelerar(self):
        for speed in range(1,26):
            velocidade = speed * 10
            print(velocidade)
            if velocidade >= 180:  
                print(f'Atingiu a velocidade maxima: {velocidade}')
                break

    def frear(self):
        speed = 180
        sub = 20
        for i in range(speed, -1, - sub):
            print(i)
            if i <= 0:
                print(f'O carro freou, velocidade atual: {i}')
                break


c1 = Carro()
c1.acelerar()
c1.frear()