class Cita:
    def __init__(self, numero=0, fecha="", hora="", descripcion="", estado=""):
        self._numero = numero
        self._fecha = fecha
        self._hora = hora
        self._descripcion = descripcion
        self._estado = estado
        
    def get_numero(self):
        return self._numero
    
    def set_numero(self, numero):
        self._numero = numero
        
    def get_fecha(self):
        return self._fecha
    
    def set_fecha(self, fecha):
        self._fecha = fecha
        
    def get_hora(self):
        return self._hora
    
    def set_hora(self, hora):
        self._hora = hora
        
    def get_descripcion(self):
        return self._descripcion
    
    def set_descripcion(self, descripcion):
        self._descripcion = descripcion
        
    def get_estado(self):
        return self._estado
    
    def set_estado(self, estado):
        self._estado = estado