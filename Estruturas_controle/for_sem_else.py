PALAVRAS_PROIBIDAS = ('corinthians','futebol', 'amor')
textos = [
    'Luan gosta do corinthians e de futebol',
    'A praia foi muito boa!',
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui uma palavra proibida: ', palavra)
            found = True
            break

if not found:
    print('Texto autorizado: ', texto)