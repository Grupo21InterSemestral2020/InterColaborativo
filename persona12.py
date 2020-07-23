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

persona1 = Persona12("Paola Nahomi Hinojosa Lozano","18","Gpe")

persona1.imprimirInfo()



