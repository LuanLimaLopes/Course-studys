def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'Kwargs: {kwargs}')

if __name__ == "__main__":
    todos_params('A', 'b', 'c')
    todos_params(1,2,3, legal=True, valor=12.99)
    todos_params('Ana', False, [1,2,3], tamanho="m", fragil=False)