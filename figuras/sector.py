class Sector
  def __init__(self,pin,radioCuadrado,numGrados):
      self.__pin = pin
      self.__radioCuadrado = radioCuadrado
      self.__numGrados = numGrados

@property
def pin(self):
    return self.__pin
@pin.setter
def pin(self, valor):
    self.__ pin = valor

@property
def radioCuadrado(self):
    return self.__radioCuadrado
@radioCuadrado.setter
def radioCuadrado(self, valor):
    self.__ radioCuadrado = valor

@property
def numGrados(self):
    return self.__numGrados
@numGrados.setter
def numGrados(self, valor):
    self.__ numGrados = valor

def area(self):
    area = self.__pin * self.__radioCuadrado * self.__numGrados /360
    return area

def ImpInf (self):
    a= (f'Datos del sector:\nPin:{self.__pin}\nRadioCuadrado:{self.__radioCuadrado}\nNumGrados:{self.__numGrados}\n El area es:{self.area()}')
    print(a)
