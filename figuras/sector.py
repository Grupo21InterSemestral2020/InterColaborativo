class Sector:
    def __init__(self,pi,radioCuadrado,numGrados):
      self.__pi = pi
      self.__radioCuadrado = radioCuadrado
      self.__numGrados = numGrados

    @property
    def pi(self):
        return self.__pi
    @pi.setter
    def pi(self, valor):
        self.__pi = valor

    @property
    def radioCuadrado(self):
        return self.__radioCuadrado
    @radioCuadrado.setter
    def radioCuadrado(self, valor):
        self.__radioCuadrado = valor

    @property
    def numGrados(self):
        return self.__numGrados
    @numGrados.setter
    def numGrados(self, valor):
        self.__numGrados = valor

    def area(self):
        area = (self.__pi * self.__radioCuadrado * self.__numGrados) /360
        return area

    def ImpInf (self):
        a= (f'Datos del sector:\nPin:{self.__pi}\nRadioCuadrado:{self.__radioCuadrado}\nNumGrados:{self.__numGrados}\n El area es:{self.area()}')
        print(a)
