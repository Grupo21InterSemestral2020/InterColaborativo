class Circulo:
    def __init__(self,pi,radio):
        self.__pi = pi
        self.__radio = radio

     @property
     def pi(self):
        return self.__pi

     @pi.setter
     def pi(self,valor):
        self.__pi = valor
