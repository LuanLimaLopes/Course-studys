PALAVRAS_PROIBIDAS = ('corinthians','futebol', 'amor')
textos = [
    'Luan gosta do e de futebol',
    'A praia foi muito boa! amor',
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui uma palavra proibida: ', palavra)
            break
    else:
        print('Texto autorizado: ', texto)