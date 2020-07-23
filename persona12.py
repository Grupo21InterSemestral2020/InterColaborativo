class Persona12:
    def __init__(self,nombre,edad,municipio):
        self.__nombre = nombre
        self.__edad = edad
        self:__municipio = municipio

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor 

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

    def imprimirInfo(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}, Municipio: {self.__municipio}")

    def obtenerEtapa(self):
        if self.__edad <=10:
            print("Niñez")
        elif self.__edad ==11 and self.__edad <=18:
            print("Adolescencia")
        elif self.__edad ==18 and self.__edad <=40:
            print("adulto")
        elif self.__edad >40:
            print("Adulto Mayor")


            
            






