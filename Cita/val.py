from datetime import datetime
import os
import time

def intPositivos(msg):
    while True:
        valor=input(msg)
        if valor.isdigit()==False:
            print("Dato invalido")
        else:
            break
    return int(valor)

def limpiar_consola():
    time.sleep(0.3) 
    if os.name == 'nt':  
        os.system('cls') 

def fecha(msg):
    while True:
        valor = input(msg)
        try:
            datetime.strptime(valor, "%d/%m/%Y").date()
            return valor
        except ValueError:
            print("Formato de fecha inválido. Use el formato DD/MM/YYYY.")
            
def hora(msg):
    while True:
        valor = input(msg)
        try:
            datetime.strptime(valor, "%H:%M").time()
            return valor
        except ValueError:
            print("Formato inválido. Por favor use formato HH:MM")
            
def Str(msg):
    while True:
        valor=input(msg).strip()
        if len(valor)==0:
            print("Debe llenar lo solicitado")
        else:
            break
    return valor

def vSioNo(msg):
    while True:
        respuesta = input(msg).strip().lower()
        if respuesta in ("s", "si", "sí"): #Para q admita variantes de S
            return "S"
        if respuesta in ("n", "no"): #Para q admita mas variantes de N
            return "N"
        print("Respuesta inválida. Responda con S o N.")