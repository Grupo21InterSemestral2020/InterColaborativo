class persona17:
    def __init__(self,nombre,edad, municipio):
        self.__nombre = nombre
        self.__edad = edad
        self.__municipio = municipio

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        self.__edad = valor

    @property
    def municipio(self):
        return self.__municipio

    @municipio.setter
    def municipio(self, valor):
        self.__municipio = valor

    def imprimirInfo(self):
        print(f"Nombre: {self.__nombre}\n Edad: {self.__edad}\n Municipio:{self.__municipio}")
    
    def ObtenerEtapa(self):
        if self.__edad >=0 and self.__edad <=11:
            print("Etapa: Niño")
        elif self.__edad >= 11 and self.__edad <=17:
            print("Etapa:Adolescente")
        elif self.__edad >=17 and self.__edad <=50:
            print("Etapa:Adulto")
        elif self.__edad >=51:
            print("Etapa:Adulto Mayor")
        else:
            print("!ERROR!")

person = Persona17("Edgar Eduardo Arriaga Martinez",21,"Monterrey")
person.imprimirInfo()
person.obtenerEtapa()