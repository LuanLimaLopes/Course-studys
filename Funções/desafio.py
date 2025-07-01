#!/usr/local/bin/python3

# resultado esperado
# <p class="alert"><span> Curso de python 3, por </span><strong id="jf"> Juracy filho</strong><span><strong id="ll"> Leonardo leitão</strong><span>.</span></p>
    #Minha tentativa (errada)
    #tag = 'strong' if args else 'spam'
    #html = args if not callable(kwargs) else args(*args, **kwargs)
    #return f'<p {kwargs}> {tag} {html}</{tag}> </p>'  

def tag(tag,*args, **kwargs,):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')
    atributos = ''.join(f'{k}="{v}"' for k, v in kwargs.items())
    inner = ''.join(args)
    return f'<{tag} {atributos}> {inner}</{tag}>'



if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'curso de Python 3, por'),
            tag('strong', 'Juracy filho', id='jf'),
            tag('span', ' e '),
            tag('strong', 'Leonardo Leitão', id='ll'),
            tag('span', '.'),
            html_class='alert')
    )