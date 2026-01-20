from datetime import datetime
import os
import time

def limpiar_consola():
    time.sleep(0.3) 
    if os.name == 'nt':  
        os.system('cls') 
def intPositivos(msg):
    while True:
        valor=input(msg)
        if valor.isdigit()==False:
            print("Dato invalido")
        else:
            break
    return int(valor)
        
def vSioNo(msg):
    while True:
        respuesta = input(msg).strip().lower()
        if respuesta in ("s", "si", "sí"): #Para q admita variantes de S
            return "S"
        if respuesta in ("n", "no"): #Para q admita mas variantes de N
            return "N"
        print("Respuesta inválida. Responda con S o N.")