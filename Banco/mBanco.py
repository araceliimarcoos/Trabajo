from cuenta import cuenta
import val

cuentas = []

def buscarCuenta(num):
    for c in cuentas:
        if c.get_numero() == num:
            return c
    return None

def Apertura():
    num = 1 + len(cuentas)
    print(f"\n--- APERTURA DE CUENTA ---")
    print(f"Su numero de cuenta es: {num}")
    
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
    cuentas.append(nueva_cuenta)
    print(f"Cuenta de {titular} creada exitosamente")
    input("    Presione Enter para continuar...")
    val.limpiar_consola()
    
def ConsultarSaldo():
    num = val.intPositivos("Ingrese número de cuenta: ")
    c = buscarCuenta(num)
    
    if c:
        print(f"Titular: {c.get_titular()} | Tipo: {c.get_tipo()}")
        print(f"Estado: {c.get_estado()} | Saldo actual: ${c.get_saldo():.2f}")
        input("    Presione Enter para continuar...")
        val.limpiar_consola() 
        
    else:
        print("Cuenta no encontrada.")
        input("    Presione Enter para continuar...")
        val.limpiar_consola()

def Deposito():
    num = val.intPositivos("Ingrese número de cuenta: ")
    c = buscarCuenta(num)
    if c:
        if c.get_estado() == "Cancelada":
            print("La cuenta ya está cancelada")
            input("    Presione Enter para continuar...")
            val.limpiar_consola()
            return
        else:
            while True:
                monto = val.vFloat("Monto a depositar: ")
                if monto > 0:
                    break
                else:
                    print("El monto debe ser mayor a 0")
            nuevo_saldo = c.get_saldo() + monto
            c.set_saldo(nuevo_saldo)
            print(f"Depósito realizado. Nuevo saldo: ${nuevo_saldo:.2f}")
            input("    Presione Enter para continuar...")
            val.limpiar_consola()
        
    else:
        print("Cuenta no encontrada")
        input("    Presione Enter para continuar...")
        val.limpiar_consola()

def Retiro():
    num = val.intPositivos("Ingrese número de cuenta: ")
    c = buscarCuenta(num)
    if c:
        if c.get_estado() == "Cancelada":
            print("La cuenta ya esta cancelada")
            input("    Presione Enter para continuar...")
            val.limpiar_consola()
            return
        else:
            monto = val.vFloat("Monto a retirar: ")
            if monto <= c.get_saldo():
                nuevo_saldo = c.get_saldo() - monto
                c.set_saldo(nuevo_saldo)
                print(f"Retiro exitoso. Saldo restante: ${nuevo_saldo:.2f}")
                input("    Presione Enter para continuar...")
                val.limpiar_consola()
            else:
                print("Dinero insuficiente")
                input("    Presione Enter para continuar...")
                val.limpiar_consola()
    else:
        print("Cuenta no encontrada")
        input("    Presione Enter para continuar...")
        val.limpiar_consola()

def Cancelacion():
    num = val.intPositivos("Ingrese número de cuenta a cancelar: ")
    c = buscarCuenta(num)
    if c:
        confirmar = val.vSioNo("Cancelar cuenta? (S/N): ")
        if confirmar == "S":
            c.set_estado("Cancelada")
            print(f"La cuenta {num} ha sido cancelada.")
            input("    Presione Enter para continuar...")
            val.limpiar_consola()
    else:
        print("Cuenta no encontrada")
        input("    Presione Enter para continuar...")
        val.limpiar_consola()
