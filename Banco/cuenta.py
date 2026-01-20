class cuenta:
    def __init__(self, numero, titular, tipo ="", saldo=0, fecha=None, estado="Activa"):
        self.__numero = numero
        self.__titular = titular
        self.__tipo = tipo
        self.__saldo = saldo
        self.__fecha = fecha
        self.__estado = estado
        
    def get_numero(self):
        return self.__numero
    
    def get_titular(self):
        return self.__titular
    
    def get_tipo(self):
        return self.__tipo
    
    def get_saldo(self):
        return self.__saldo
    
    def get_fecha(self):
        return self.__fecha
    
    def get_estado(self):
        return self.__estado
    
    def set_numero(self, numero):
        self.__numero = numero
        
    def set_titular(self, titular):
        self.__titular = titular
        
    def set_tipo(self, tipo):
        self.__tipo = tipo
        
    def set_saldo(self, saldo):
        self.__saldo = saldo
        
    def set_fecha(self, fecha):
        self.__fecha = fecha
        
    def set_estado(self, estado):
        self.__estado = estado