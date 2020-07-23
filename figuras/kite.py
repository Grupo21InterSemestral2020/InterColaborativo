class Kite:
    def __init__(self,diagonalE,diagonalF):
        self.__diagonalE=diagonalE
        self.__diagonalF=diagonalF
    
    @property
    def diagonalE(self):
        return self.__diagonalE
    
    @diagonalE.setter
    def diagonalE(self,valor):
        self.__diagonalE=valor
    
    @property
    def diagonalF(self):
        return self.__diagonalF
    
    @diagonalF.setter
    def diagonalF(self,valor):
        self.__diagonalF=valor
    
