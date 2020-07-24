class Cuadrilatero:
    def __int__(self, Lado1, Lado2, Sen):
        self.__Area= Area
        self.__Lado1= Lado1
        self.__Lado2= Lado2 
        self.__Sen= Sen
        
        
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
    def Sen (self):
        return self.__Area

    @Sen.setter
    def Sen (self, valor):
        self._Sen= valor

     def Area(self):
        Area = self.__Lado1 * self.__Lado2 * self.__Sen
        return Area
    
    def ImprimirInfo(self):
        RESULTADO = (f"Cuadrilatero: Lado1:{self.__Lado1} Lado2: {self.__Lado2} Sen:{self.__Sen} El Area es {self.Area()}")
        print(RESULTADO)

        



