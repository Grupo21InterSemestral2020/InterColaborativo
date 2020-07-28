class Persona10:
    def __init__(self,nombre,edad,municipio):
        self.__nombre = nombre
        self.__edad = edad
        self.__municipio = municipio

    @property
    def nombre (self):
        return self.__nombre 

    @nombre.setter
    def nombre (self,valor1):
        self.__nombre = valor1

    @property
    def edad (self):
        return self.__edad

    @edad.setter
    def edad (self,valor2):
        self.__edad = valor2

    @property
    def municipio (self):
        return self.__municipio

    @municipio.setter
    def municipio (self, valor3):
        self.__municipio = valor3

    def ImprimirInfo(self):
        print (f'{self.__nombre}{self.__edad}{self.__municipio}')

    def ObtenerEtapa (self):
        if self.__edad >= 0 and self.__edad <=10:
            print ("Niño")
        elif self.__edad >=11 and self.__edad <=17:
            print("Adoloscente")
        elif self.__edad >=18 and self.__edad <=40:
            print ("Adulto")
        elif self.__edad >40:
            print("Adulto mayor")
        else:
            print("Error")
