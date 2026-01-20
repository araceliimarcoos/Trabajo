"""Se requiere modelar un sistema abstracto para administrar
cuentas bancarias.
Cada cuenta bancaria debe contar con un número de cuenta
único, nombre del titular, tipo de cuenta, saldo, fecha de
apertura y estado de la cuenta.

Las operaciones mínimas que debe permitir el sistema son:

apertura de cuenta

consulta de saldo

depósito

retiro

cancelación de cuenta"""

import mBanco
import val

opc = -1
while opc != 0:
    print("\n--- SISTEMA BANCARIO ---")
    print("1. Apertura de cuenta\n2. Consulta de saldo\n3. Depósito\n4. Retiro\n5. Cancelación de cuenta\n0. Salir")
    
    opc = val.intPositivos("\nSeleccione una opcion: ")
    match opc:
        case 1: 
            mBanco.Apertura()
            
        case 2: 
            mBanco.ConsultarSaldo()
            
        case 3: 
            mBanco.Deposito()
            
        case 4: 
            mBanco.Retiro()
            
        case 5: 
            mBanco.Cancelacion()
            
        case 0: 
            print("Saliendo...")
                
