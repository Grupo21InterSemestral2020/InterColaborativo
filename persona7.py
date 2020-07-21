class persona7:
    def __init__(Nombre,edad,municipio):
        self.__Nombre = Nombre
        self.__edad = edad
        self.__municipio = municipio

    @property
    def Nombre(self):
        return self.__Nombre

    @Nombre.setter
    def Nombre(self,valor):
        self.__Nombre = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,valor):
        self.__edad = valor

    @property
    def municipio(self):
        return self.__municipio

    @municipio.setter
    def municipio(self,valor):
        self.__municipio = valor

    def imprimir(self):
        print(f"Nombre: {self.__Nombre},edad: {self.__edad},municipio: {self.__municipio}")




