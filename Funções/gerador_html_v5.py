#!/usr/local/bin/python3
bloco_atributos = ('bloco_acesskey', 'bloco_id')
ul_atributos = ('ul_id', 'ul_style')

def filtrar_atributos(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}= "{v}"'
        for k, v in informados.items() if k in suportados)

def tag_bloco(conteudo, *args, classe ='sucess', inline=False, **novos_atributos):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **novos_atributos)
    atributos = filtrar_atributos(novos_atributos, bloco_atributos)

    return f'<{tag} {atributos} class="{classe}"> {html}</{tag}>'

def tag_list(*itens, **novos_atributos):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul {filtrar_atributos(novos_atributos, ul_atributos)}>{lista}</ul>'

if __name__ == '__main__':
    print(tag_bloco(tag_list, 'Sol', 'Lua', classe='info', inline=True))

    print(tag_bloco(tag_list, 'Item 1', 'item 2', classe='sucess', bloco_acesskey='m', bloco_id='conteudo'))