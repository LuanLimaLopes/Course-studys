PALAVRAS_PROIBIDAS = {'corinthians', 'politica', 'santos', 'fortaleza'}
textos = [
    'Luan gosta do corinthians do santos e do fortaleza',
    'Luan gosta do curitiba',
]

for texto in textos:
   intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
   if intersecao:
      print(f'Texto possui palavras proibidas: {intersecao}')
   else:
      print(f'Texto autorizado : "{texto}"')