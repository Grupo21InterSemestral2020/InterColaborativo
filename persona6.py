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

    def imprimirInfo(self):
        print(f"Nombre: {self.__nombre}\n Edad: {self.__edad}\n Municipio:{self.__municipio}")

    def obtenerEtapa(self):
        if self.__edad >= 0 and self.__edad <= 10:
            print("Etapa Niño")
        elif self.__edad >= 11 and self.__edad <= 17:
            print("Etapa Adolescente") 
        elif self.__edad >= 18 and self.__edad <= 40:
            print("Etapa Adulto")
        elif self.__edad > 40:
            print("Etapa Adulto Mayor")
        else:
            print("Edad Incorrecta")

P6 = Persona6("Johan Alexis Balleza",22,"Apodaca")

P6.imprimirInfo()
P6.obtenerEtapa()