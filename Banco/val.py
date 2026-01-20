import time
import os
import datetime
def intPositivos(msg):
    while True:
        valor=input(msg)
        if valor.isdigit()==False:
            print("Dato Invalido. Por favor ingrese un numero")
        else:
            break
    return int(valor)

def vFloat(msg):
    while True:
        valor = input(msg)
        aux = valor.replace(".","") # quitar temporalmete el .
        if aux.isdigit() == False:
            print("dato invalido")
        else:
            break
    return float(valor)

def vSioNo(msg):
    while True:
        respuesta = input(msg).strip().lower()
        if respuesta in ("s", "si", "sí"): #Para q admita variantes de S
            return "S"
        if respuesta in ("n", "no"): #Para q admita mas variantes de N
            return "N"
        print("Respuesta inválida. Responda con S o N.")

def Str(msg):
    while True:
        valor = input(msg)
        if len(valor) == 0:
            print("Debe llenar lo solicitado")
        else:
            if len(valor) <2:
                print("Minimo 2 letras o numeros")
            else:
                break
    return valor

def fecha(msg):
    while True:
        valor = input(msg)
        try:
            datetime.datetime.strptime(valor, "%d/%m/%Y").date()
            return valor
        except ValueError:
            print("Formato de fecha inválido. Use el formato DD/MM/YYYY.")
            
def limpiar_consola():
    time.sleep(0.3)
    if os.name == 'nt':  
        os.system('cls') 