#!/usr/local/bin/python3

def tag_bloco(texto, classe ='sucess', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}"> {texto}</{tag}>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('Teste', 'teste classe', True))
    # Aula de Parâmetros nomeados ->
    print(tag_bloco(inline=False, texto='Nomenclatura', classe='Informa'))