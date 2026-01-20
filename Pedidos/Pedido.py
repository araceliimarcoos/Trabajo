class Pedido:
    def __init__(self, PedidoID=0, NombrePropie="", platilloID=0):
        self.__pedidoID=PedidoID
        self.__NombrePropietario=NombrePropie
        self.__platilloID= platilloID
        self.__HoraEntrega=HoraEntrega
        
    def __str__(self):  
        return f"{self.__pedidoID}{self.__NombrePropietario}{self.__platilloID}"
    
    def get_PedidoID(self):
        return self.__pedidoID
    def set_PedidoID(self, pedidoID):
        self.__pedidoID=pedidoID
    
    def get_NombrePropietario(self):
        return self.__NombrePropietario
    def set_NombrePropietario(self, NombrePropietario):
        self.__NombrePropietario=NombrePropietario
        
    def get_platilloID(self):
        return self.__platilloID
    def set_platillo(self, platilloID):
        self.__platilloID
