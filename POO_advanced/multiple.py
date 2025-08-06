#!/usr/local/bin/python3

class Animal:
    @property
    def capabilities(self):
        return ('sleep', 'eat', 'drink')
    

class Human(Animal):
    @property
    def capabilities(self):
        return super().capabilities + ('love', 'talk', 'study')
    
class Spider(Animal):
    @property
    def capabilities(self):
        return super().capabilities + ('make web','Walk through walls')
    
class SpiderMan(Spider, Animal):
    @property
    def capabilities(self):
        return super().capabilities + ('beat up bandits','shoot webs at buildings')
    
if __name__ == '__main__':
    john = Human()
    print(f'Jonh: {john.capabilities}')
    spider = Spider()
    print(f'Spider: {spider.capabilities}')

    peter = SpiderMan()
    print(f'Peter Parker: {peter.capabilities}')