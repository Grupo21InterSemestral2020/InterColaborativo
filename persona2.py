class Persona2:

    def __init__(self, nombre, edad, municipio):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def nombre(self, valor):
        self.__edad = valor

    @property
    def minicipio(self):
        return self.__municipio

    @municipio.setter
    def municipio(self, valor):
        self.__municipio = valor

