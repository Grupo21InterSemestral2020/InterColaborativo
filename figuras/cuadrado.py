class Cuadrado:
    def __init__(self,lado):
        self.__lado = lado
    
    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self,lado):
        self.__lado = lado

    def area(self,area,lado):
        print("Lado del cuadrado:")
        area = lado * lado
    
    def imprimirInfo(self,area):
        print(f'su area es: {area}')
    