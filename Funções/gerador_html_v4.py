#!/usr/local/bin/python3

def tag_bloco(conteudo, *args, classe ='sucess', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)

    return f'<{tag} class="{classe}"> {html}</{tag}>'

def tag_list(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'

if __name__ == '__main__':
    print(tag_bloco(tag_list, 'Sol', 'Lua', classe='info', inline=True))