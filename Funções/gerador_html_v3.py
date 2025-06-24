#!/usr/local/bin/python3

def tag_bloco(texto, classe ='sucess', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}"> {texto}</{tag}>'

def tag_list(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'

if __name__ == '__main__':
    print(tag_bloco(inline=False, texto='Nomenclatura', classe='Informa'))

    print(tag_bloco(tag_list('Item 1', 'Item 2'), classe='info'))