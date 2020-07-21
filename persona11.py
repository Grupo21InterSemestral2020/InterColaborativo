class Persona11:
    def __init__(self,nombre,edad,municipio):
        self._nombre = nombre
        self._edad = edad
        self._municipio = municipio
    @property
    def nombre (self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nuevoNombre):
        self.__nombre = nuevoNombre

    @property
    def edad (self):
        return self.__edad
    @edad.setter
    def edad(self,nuevoEdad):
        self.__edad = nuevoEdad

    @property
    def municipio (self):
        return self.__municipio
    @municipio.stter
    def municipio (self, nuevaMunicipio):
        self.__municipio = nuevaMunicipio

    def imprimirInfo(self)
        print(f'Persona 11,=nombre :{self.__nomre}, Edad: {self.__edad}, Municipio: {self.__municipio}')

    def obtener_etapa(self)
        if self.__edad <10:
            print("Etapa Niñez")
        elif  self.__edad >= 11 and self.__edad<=17:
            print("Etapa Adolescente")
        elif self.__edad >=18 and self.__edad<=40:
            print("Etapa Adulta")
        elif self.__edad >40:
            print("Etapa Adulta")
        else:
            print("Edad incorrecta")