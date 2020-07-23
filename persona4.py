class Persona4:
    def __init__(self,nombre,edad,municipio):
        self.__nombre=nombre
        self.__edad=edad
        self.__municipio=municipio

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,valor):
        self.__nombre= valor
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,valor):
        self.__edad=valor
    
    @property
    def municipio (self):
        return self.__municipio
    
    @municipio.setter
    def municipio(self,valor):
        self.__municipio=valor

    def ImprimirInfo(self):
        print(f'Nombre:{self.__nombre}\nEdad:{self.__edad}\nMunicipio:{self.__municipio}')
    
    def ObtenerEtapa(self):
        if self.__edad >=0 and self.__edad <=12:
            print("Etapa: Niño")
        elif self.__edad >= 12 and self.__edad <=17:
            print("Etapa:Adolescente")
        elif self.__edad >=18 and self.__edad <=40:
            print("Etapa:Adulto")
        elif self.__edad >=41:
            print("Etapa:Adulto Mayor")

personax = Persona4("Alejandro",21,"Mty")
personax.ImprimirInfo()
personax.ObtenerEtapa()



