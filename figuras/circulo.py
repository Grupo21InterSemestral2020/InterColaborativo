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

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self,valor2):
        self.__radio= valor2

    def area(self):
        area = self.__pi * self.__radio
        return area

    def imprimirInfo(self):
        print(f'El area del circulo:\n pi = {self.__pi}\n radio = {self.__radio}')