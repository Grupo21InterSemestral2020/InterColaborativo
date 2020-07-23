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