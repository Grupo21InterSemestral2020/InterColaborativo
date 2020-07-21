class Persona10:
    def _init_(self,nombre,edad,municipio):
        self.__nombre = nombre
        self.__edad = edad
        self.__municipio = municipio
    @property 
    def nombre (self):
     return self.__nombre

    @nombre.setter
    def nombre (self,nombre10):
        self.__nombre = nombre10

    @property
    def edad (self):
        return self.__edad
    
    @setter.edad
    def edad (self,edad10):
        self._edad = edad10

    @property
    def municipio(self):
        return self.__municipio   

    @setter.municipio
    def municipio (self,municipio10)
    self.__municipio = municipio10