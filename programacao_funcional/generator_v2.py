from generator_v1 import colors_arco_iris

if __name__ == '__main__':
    generator = colors_arco_iris()
    for cor in generator:
        print(cor)
    print('Fim!')