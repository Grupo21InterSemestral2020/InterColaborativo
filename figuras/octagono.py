class octagono:
    def __init__(self,longitud,perimetro,apotema):
        self.__longitud = longitud
        self.__perimetro = perimetro
        self.__apotema = apotema

    @property
    def longitud(self):
        return self.__longitud

    @longitud.setter
    def longitud(self,valor1):
        self.__longitud = valor1

    @property
    def perimetro(self):
        return self.__perimetro

    @perimetro.setter
    def perimetro(self,valor2):
        self.__perimetro = valor2

    @property
    def apotema(self):
        return self.__apotema

    @apotema.setter
    def apotema(self,valor3):
        self.__apotema = valor3

    def ImprimirInfo(self):
        print("perimetro: {self.__longitud},apotema: {self.__apotema}")

    def area(self):
        area = self.__perimetro * self.__apotema/2



