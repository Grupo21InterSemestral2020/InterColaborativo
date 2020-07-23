class Poligono:
    def __init__(self,nLado,aLongitud):
        self.__nLado = nLado
        self.__aLongitud = aLongitud
        
    @property
    def nLado (self,):
        return self.__nLado

    @nLado.setter
    def nLado (self,nLado):
        self.__nLado = nLado

    @property
    def aLongitud (self):
        return self.__aLongitud

    @aLongitud.setter
    def aLongitud (self,aLongitud):
        self.__aLongitud = aLongitud

    def area (self):
        area = self.__nLado * self.__aLongitud**2  * (3.14/self.__nLado) / 4
        return area

    def ImprimirInfo (self):
        I = (f'Poligono:\n Lado:{self.__nLado}\n aLongitud: {self.__aLongitud}\n El area del poligono es: {self.area()}')
        print(I)