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
        
    @edad.setter
    def edad (self,edad10):
        self._edad = edad10

    @property
    def municipio(self):
        return self.__municipio   

    @municipio.setter
    def municipio (self,municipio10):
        self.__municipio = municipio10
        
    def imprimirInfo(self):
        print(f'Persona 10 = Nombre:{self.__nombre}, Edad: {self.__edad}, Municipio: {self.__municipio}')
        
    def obtenerEtapa (self):
        if self.__edad >=0 and self.__edad <=10:
            print("Etapa: Niñez")
        elif self.__edad >=11 and self.__edad <= 18:
            print("Etapa: Adolescencia")
        elif self.__edad >=17 and self.__edad <= 39:
            print("Etapa: Adulto")
        elif self.__edad >40:
            print("Etapa: Adulto mayor")