class Hexagono:
    def __init__(self,perimetro,apotema):
        self.__perimetro = perimetro
        self.__apotema = apotema
    
    @property
    def perimetro(self):
        return self.__perimetro

    @perimetro.setter
    def perimetro(self,valor):
        self.__perimetro = valor
        
    @property
    def apotema(self):
        return self.__apotema
        
    @apotema.setter
    def apotema(self,valor2):
        self.__apotema = valor2
        
    def area(self):
        area = self.__perimetro * self.__apotema / 2
    
    @property
    def area(self):
        area = self.__perimetro * self.__apotema / 2
        return area
    
    def ImprimirInfo():
        return("")
        