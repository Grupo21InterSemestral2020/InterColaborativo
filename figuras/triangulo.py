class Triangulo:
    def __init__(self,base,altura):
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self,valor):
        self.__base = valor 

    @property
    def altura(self):
        return self.__altura

    @altura.setter 
    def altura(self,valor):
        self.__altura = valor 

    def imprimirInfo(self):
        print(f"base:{self.__base} \naltura:{self.__altura}")
        
    def area(self):
        area = self.__base * self.__altura /2
        print(area)

Triangulo = Triangulo(10,15)
Triangulo.imprimirInfo()
Triangulo.area()    
