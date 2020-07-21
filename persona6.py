class Persona6:
    def __init__(self,nombre,edad,municipio):
        self.__nombre = nombre
        self.__edad = edad
        self.__municipio = municipio 

    @property
    def nombre (self):
        return self.__nombre

    @property
    def edad (self):
        return self.__edad

    @property
    def municipio (self):
        return self.__municipio

    @nombre.setter
    def nombre (self,nombre1):
        self.__nombre = nombre1

    @edad.setter
    def edad (self,edad1):
        self.__edad = edad1

    @municipio.setter
    def municipio (self,municipio1):
        self.__municipio = municipio1