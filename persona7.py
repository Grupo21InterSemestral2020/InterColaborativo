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

    def imprimirInf(self):
        print(f"Nombre: {self.__Nombre},edad: {self.__edad},municipio: {self.__municipio}")

    def obtenerEtapa(self):
        if self.__edad >= 0 and self.__edad <= 10:
            print("Es niño")
        elif self.__edad >= 11 and self.__edad <= 17:
            print("Es adolescente") 
        elif self.__edad >= 18 and self.__edad <= 40:
            print("Es adulto")
        elif self.__edad > 40:
            print("Es adulto mayor")




