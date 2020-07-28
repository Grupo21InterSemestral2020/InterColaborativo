class Trapezoide:
    def __init__(self,Bmayor,Bmenor,altura):
        self.__Bmayor = Bmayor
        self.__Bmenor = Bmenor
        self.__altura = altura

    @property
    def Bmayor(self):
        return self.__Bmayor

    @Bmayor.setter
    def Bmayor(self,Basemayor):
        self.__Bmayor = Basemayor

    @property
    def Bmenor(self):
        return self.__Bmenor

    @Bmenor.setter
    def Bmenor(self,Basemenor):
        self.__Bmenor = Basemenor

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self,nuevaAltura):
        self.__altura = nuevaAltura

    def imprimirInfo(self):
        print(f'Area de trapezoide:\n BaseMayor = {self.__Bmayor}\n BaseMenor = {self.__Bmenor}\n Altura = {self.__altura}')
    
    def area(self):
        print(f'>>Area = {(self.__Bmayor + self.__Bmenor)*(self.__altura)/2}')

    