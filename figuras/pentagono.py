import math  
class Pentagono:
    def __init__(self,lado):
        self.__lado = lado

    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self,valor):
        self.__lado= valor

    def area(self):
        area = (self.__lado * self.__lado) * math.sqrt(25 + 10 * math.sqrt (5)) / 4
        return area

    def ImprimirInfo(self):
        s = (f"Pentagono:\nlado:{self.__lado}\nEl area es {self.area()}")
        print(s)

Penta= Pentagono(10)
Penta.ImprimirInfo()
 
    
