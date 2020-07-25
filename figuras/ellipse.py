class Ellipse:
    def __init__(self,pi,a,b):
        self.__pi = pi
        self.__a = a
        self.__b = b

    @property
    def pi(self):
        return self.__pi
    @pi.setter
    def pi(self, valor):
        self.__pi = valor

    @property
    def a(self):
        return self.a
    @a.setter
    def a(self, valor):
        self.__a = valor

    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, valor):
        self.__b = valor

    def area(self):
        area = self.__pi * sel.__b * self.__b
        return area

    def ImprimirInfo(self):
        a= (f'Datos de ellipse:\nPi:{self.__pi}\na:{self.__a}\nb:{self.__b}\n El area es:{self.area()}')
        print(a)