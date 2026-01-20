class Platillo:
    def __init__(self, platilloID=0, nombre="", precio=0, disponibilidad="Disponible"):
        self.__platilloID= platilloID
        self.__nombre= nombre
        self.__precio= precio
        self.__disponibilidad= disponibilidad
    def __str__(self):
        return f"{self.__platilloID} {self.__nombre} {self.__precio} {self.__disponibilidad}"
    def get_platilloID(self):
        return self.__platilloID
    def set_platilloID(self, platilloID):
        self.__platilloID = platilloID
        
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_precio(self):
        return self.__precio
    def set_precio(self, precio):
        self.__precio = precio
        
    def get_disponibilidad(self):
        return self.__disponibilidad
    def set_disponibilidad(self, disponibilidad):
        self.__disponibilidad= disponibilidad
        