class Cubo:
    def __int__(self, Lado1, Lado2, SumLd):
        self.__Area= Area
        self.__Lado1= Lado1
        self.__Lado2= Lado2 
        self.__SumLd= SumLd
        
        
     @property
    def Lado1 (self):
        return self.__Lado1

    @Lado1.setter
    def Lado1 (self, valor):
        self.__Lado1= valor

     @property
    def Lado2 (self):
        return self.__Lado2

    @Lado2.setter
    def Lado2 (self, valor):
        self.__Lado2= valor

    @property
    def SumLd (self):
        return self.__SumLd

    @SumLd.setter
    def SumLd (self, valor):
        self.__SumLd= valor

    def Area(self):
        Area = self.__Lado1 * self.__Lado2 * self.__SumLd
        return Area

    
    def ImprimirInfo(self):
        RESULTADO = (f"Cuadrilatero: Lado1:{self.__Lado1} Lado2: {self.__Lado2} SumLd:{self.__SumLd} El Area es {self.Area()}")
        print(RESULTADO)
        