class Curso:
    def __init__(self, clave=0, nombre="", maxAlumnos=0):
        self.__clave = clave
        self.__nombre = nombre
        self.__maxAlumnos = maxAlumnos
        self.__alumnos = []

    def __str__(self):
        return (f"{self.__clave} {self.__nombre} {self.__maxAlumnos}  {len(self.__alumnos)}")

    def get_clave(self):
        return self.__clave
    def set_clave(self, clave):
        self.__clave = clave

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_maxAlumnos(self):
        return self.__maxAlumnos
    def set_maxAlumnos(self, maxAlumnos):
        self.__maxAlumnos = maxAlumnos

    def get_alumnos(self):
        return self.__alumnos

   