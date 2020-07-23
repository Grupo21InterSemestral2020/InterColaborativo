class Cuadrado:
    def __init__(self,lado):
        self.__lado = lado
    
    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self,lado):
        self.__lado = lado

    