class Rectangulo:
    
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura
    
    @property
    def base(self):
        return self.__base 

    @base.setter
    def base(self, valor):
        self.__base = valor

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        self.__altura = valor

    def area(self):
        return self.__base * self.__altura

a = Rectangulo(10,10)
print(a.area())
