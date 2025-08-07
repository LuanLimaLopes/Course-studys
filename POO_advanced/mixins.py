#!/usr/local/bin/python3

class HtmlToStringMixin:
    def __str__(self):
        #Conversão para HTML   
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>')
        return f'<span>{html}</span>'
    

class People:
    def  __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name
    

class Animal:
    def __init__(self,name, pet=True):
        self.name = name
        self.pet = pet
    
    def __str__(self):
        return self.name + ' (pet)' if self.pet else ''
    
class PeopleHtml(HtmlToStringMixin, People):
    pass


class AnimalHtml(HtmlToStringMixin, Animal):
    pass


if __name__ == '__main__':
    p1 = People('Lavinia poloni')
    p2 = PeopleHtml('Luan lopes')
    print(p1)
    print(p2)

    Luna = AnimalHtml('Luna')
    print(Luna)

