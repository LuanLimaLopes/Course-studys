#!/usr/local/bin/python3

def tag_bloco(texto, classe ='sucess'):
    return f'<div class="{classe}"> {texto}</div>'


if __name__ == '__main__':
    #Testes (assertions)
    #assert tag_bloco('Teste') == \
    #    '<div class="sucess">Teste</div>'
    
    #assert tag_bloco('Impossível excluir!', 'error') == \
    #    '<div class="error">impossível excluir!</div>'
    print(tag_bloco('bloco'))