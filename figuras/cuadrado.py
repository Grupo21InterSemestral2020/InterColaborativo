class Cuadrado:
    def __init__(self,lado):
        self.__lado = lado
    
    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self,lado):
        self.__lado = lado

    def imprimirInfo(self):
        print(f'Lado: {self.__lado}')

    def area(self):
        area = self.__lado * self.__lado
        print(f'tu area es: {area}')
       
