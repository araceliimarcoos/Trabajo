class producto:
    
    def __init__(self, id = 0, name= "", price = 0, status = ""):
        self.__id = id 
        self.__name = name 
        self.__price = price
        self.__status = status
    
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price
        
    def get_status(self):
        return self.__status
    def set_status(self, status):
        self.__status =status
        

