class Persona5():
    def __init__(self,nombre,edad,municipio):
        self.__nombre = nombre
        self.__edad = edad
        self.__municipio = municipio
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevoNombre):
        self.__nombre = nuevoNombre

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,nuevaEdad):
        self.__edad = nuevaEdad

    @property
    def municipio(self):
        return self.__municipio
    
    @municipio.setter
    def municipio(self,nuevoMunicipio):
        self.__municipio = nuevoMunicipio
    