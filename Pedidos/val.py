import time
import os
def intPositivos(msg):
    while True:
        valor=input(msg)
        if valor.isdigit()==False:
            print("Dato Invalido. Por Favor ingrese un numero")
        else:
            break
    return int(valor)
def Str(msg):
    while True:
        txt=input(msg)
        if len(txt)<=1:
            print("Debe tener al menos 2 letras")
        else:
            break
    return str(txt)

def limpiar():
    time.sleep(0.3)
    if os.name == 'nt':  
        os.system('cls') 