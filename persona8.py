class Persona8:
    def _int_(self, nombre, edad, municipio):
        self._nombre= nombre
        self._edad= edad
        self._municipio= municipio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre= valor

    

