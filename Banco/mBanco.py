from cuenta import cuenta
import val

# Diccionario para almacenar cuentas {numero: objeto_cuenta}
cuentas = {}

def Apertura():
    num = 1 + len(cuentas) 
    print(f"\n--- APERTURA DE CUENTA ---")
    print(f"Su nuevo número de cuenta asignado es: {num}")
    
    titular = val.Str("Nombre del titular: ")
    while True:
        op = val.intPositivos("Tipo de cuenta (1. Ahorro 2. Corriente): ")
        if op == 1:
            tipo = "Ahorro"
            break
        elif op == 2:
            tipo = "Corriente"
            break
        else:
            print("Opción no disponible.")
        
    while True:
        saldo_inicial = val.vFloat("Saldo inicial: ")
        if saldo_inicial > 0:
            break
        else:
            print("El saldo inicial debe ser mayor a 0.")
    fecha = val.fecha("Fecha de apertura (dd/mm/aaaa): ")
    
    nueva_cuenta = cuenta(num, titular, tipo, saldo_inicial, fecha)
    cuentas[num] = nueva_cuenta
    print(f"Cuenta de {titular} creada exitosamente")

def ConsultarSaldo():
    num = val.intPositivos("Ingrese número de cuenta: ")
    if num in cuentas:
        c = cuentas[num]
        print(f"Estado: {c.get_estado()} | Saldo actual: ${c.get_saldo():.2f}")
    else:
        print("Cuenta no encontrada.")

def Deposito():
    num = val.intPositivos("Ingrese número de cuenta: ")
    if num in cuentas:
        if cuentas[num].get_estado() == "Cancelada":
            print("Operación denegada. La cuenta está cancelada.")
            return
        while True:
            monto = val.vFloat("Monto a depositar: ")
            if monto > 0:
                break
            else:
                print("El monto debe ser mayor a 0")
        nuevo_saldo = cuentas[num].get_saldo() + monto
        cuentas[num].set_saldo(nuevo_saldo)
        print(f"Depósito realizado. Nuevo saldo: ${nuevo_saldo:.2f}")
    else:
        print("Cuenta no encontrada.")

def Retiro():
    num = val.intPositivos("Ingrese número de cuenta: ")
    if num in cuentas:
        if cuentas[num].get_estado() == "Cancelada":
            print("Operación cancelada. La cuenta ya esta cancelada")
            return
        monto = val.vFloat("Monto a retirar: ")
        if monto <= cuentas[num].get_saldo():
            nuevo_saldo = cuentas[num].get_saldo() - monto
            cuentas[num].set_saldo(nuevo_saldo)
            print(f"Retiro exitoso. Saldo restante: ${nuevo_saldo:.2f}")
        else:
            print("Fondos insuficientes.")
    else:
        print("Cuenta no encontrada.")

def Cancelacion():
    num = val.intPositivos("Ingrese número de cuenta a cancelar: ")
    if num in cuentas:
        cuentas[num].set_estado("Cancelada")
        print(f"La cuenta {num} ha sido cancelada.")
    else:
        print("Cuenta no encontrada.")