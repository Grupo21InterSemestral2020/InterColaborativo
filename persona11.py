class Persona11:
    def __init__(self,nombre,edad,municipio):
        self._nombre = nombre
        self._edad = edad
        self._municipio = municipio
    @property
    def nombre (self):
        return self.__nombre
    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor

    @property
    def edad (self):
        return self.__edad
    @edad.setter
    def edad(self,valor):
        self.__edad = valor

    @property
    def municipio (self):
        return self.__municipio
    @municipio.stter
    def municipio (self, valor):
        self.__municipio = valor

