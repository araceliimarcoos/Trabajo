class Libros:
    def __init__(self, id=0, titulo="", autor="", estado=""):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__estado = 'Disponible'
    
    def __str__(self):
        return f"{self.__id} {self.__titulo} {self.__autor} {self.__estado}"
    
    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    
    def get_autor(self):
        return self.__autor
    
    def set_autor(self, autor):
        self.__autor= autor
        
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id
        
    def get_estado(self):
        return self.__estado
    
    def set_estado(self, estado):
        self.__estado = estado