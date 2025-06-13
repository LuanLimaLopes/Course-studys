#!/usr/local/bin/python3

def fibonnaci():
    penultimo = 0
    ultimo = 1
    print(f"{penultimo},{ultimo}", end=',')
    while True:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonnaci()