class Usuarios:
    def __init__(self, id=0, nombre="", apellido1="", apellido2=""):
        self.__id = id
        self.__nombre = nombre
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
    
    def __str__(self):
        return f"{self.__id} {self.__nombre} {self.__apellido1} {self.__apellido2}"
    
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_apellido1(self):
        return self.__apellido1
    
    def set_apellido1(self, apellido1):
        self.__apellido1= apellido1
    
    def get_apellido2(self):
        return self.__apellido2
    
    def set_apellido2(self, apellido2):
        self.__apellido2= apellido2
    