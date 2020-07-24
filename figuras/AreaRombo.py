class Rombo(object):
    def__init__(self,dmayor,dmenor):
        self.__dmayor = dmayor
        self.__dmenor = dmenor
        
    @property
    def dmayor(self):
        return self.__dmayor

    @dmayor.setter
    def dmayor(self,valor):
        self.__dmayor = valor
        
    @property
    def dmenor(self):
         return self.__dmenor

    @dmenor.setter
     def dmenor(self,valor2):
         self.__dmenor = valor2

     def ImprimirInfo(self):
         print(f"dmayor:{self.__dmayor}\n dmenor:{self.__dmenor}")

     def area(self):
         area = self.__dmayor * self.__dmenor /2
         print("Su area es: ")





