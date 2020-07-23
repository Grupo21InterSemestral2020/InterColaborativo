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

    def imprimirInfo(self):
        return (f"\n>>>La base del rectangulo es: {self.__base}\n>>>La altura del rectangulo es: {self.__altura}\n")

    def area(self):
        return self.__base * self.__altura
