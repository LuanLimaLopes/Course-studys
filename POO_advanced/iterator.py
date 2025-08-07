#!/usr/local/bin/python3


class RGB:
    def __init__(self):
        self.cores = ['Red', 'Blue', 'Green'][::-1]

    def __next__(self):
        try:
            return self.cores.pop()
        except IndexError:
            raise StopIteration()
        
    
if __name__ == '__main__':
    cores = RGB()
    print(next(cores))
    print(next(cores))
    print(next(cores))

    try:
        print(next(cores))
    except StopIteration:
        print('Acabou as cores!')