class trapezoide:
    def __init__(self,Bmayor,Bmenor):
        self.__Bmayor = Bmayor
        self.__Bmenor = Bmenor

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

    def imprimirInfo(self):
        print(f'Area de trapezoide:\n BaseMayor = {self.__Bmayor}\n BaseMenor = {self.__Bmenor}')
    
    def area(self):
        print((self.__Bmayor * self.__Bmenor)/2)

    