class Paralelogramo:
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
        return self.__altura3
        
    @altura.setter
    def altura(self,valor2):
        self.__altura = valor2
        
    def area(self):
        area = self.__base * self.__altura
        return area
    
    def ImprimirInfo(self):
        s = (f"Paralelogramo:\nBase:{self.__base}\nAltura: {self.__altura}\nEl area es {self.area()}")
        print(s)
        