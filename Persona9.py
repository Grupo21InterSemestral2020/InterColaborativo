class Persona9:
    def __init__(self,nombre,edad,municipio):
        self.__nombre = nombre
        self.__edad = edad
        self.__municipio = municipio
    
@property
def nombre(self):
    return self.__nombre

@nombre.setter
def nombre(self, nuevoNombre):
    self.__nombre = nuevoNombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nuevaEdad):
        self.__edad = nuevaEdad

    @property
    def municipio(self):
        return self.__municipio

    @municipio.setter
    def municipio(self, nuevoMunicipio):
        self.__municipio = nuevoMunicipio

    def imprimirInfo(self):
        print(f'Persona 10 = Nombre:{self.__nombre}, Edad: {self.__edad}, Municipio: {self.__Municipio}')

    def obtener_etapa(self):
        if self.__edad < 10:
            print("Etapa: Niñez")
        elif (self.__edad) >=11 and (self.__edad) <= 18
            print("Etapa: Adolescencia")
        elif (self.__edad >=18) and (self.__edad <= 40)
            print("Etapa: Adulto")
        elif (self.__edad) >40
            print("Etapa: Adulto mayor")