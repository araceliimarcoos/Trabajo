''' Se desea modelar un pedido de restaurante.
Un pedido está compuesto por varios platillos.
Cada platillo tiene nombre, precio y disponibilidad.
El pedido puede estar abierto, cerrado o cancelado.
-agregar platillo
-eliminar platillo
-calcular total
- cerrer pedido'''
from DPlatillos import Platillos
from Platillo import Platillo
import val
pedido=[]
cliente=""
def mostrarmenu():
    print("---- MENU -----")
    for p in Platillos:
        print(f"{p.get_platilloID()} - {p.get_nombre()} (${p.get_precio()}) [{p.get_disponibilidad()}]")
    
def agregarPlatillo():
    mostrarmenu()
    id=int(val.intPositivos("Seleccione el numero del platillo: "))
    for p in Platillos:
        if p.get_platilloID()==id:
            if p.get_disponibilidad()=="Disponible":
                pedido.append(p)
                print("\nPLATILLO AGREGADO AL PEDIDO")
                
            else:
                print("\nPLATILLO NO DISPONIBLE")
            input("\nPresione Enter ppara Continuar...")
            return
    
    print("No se encontro platillo con ese ID")
    
def mostrarPedido():
    if not pedido:
        print("\nPedido vacío")
        return

    print("Pedido de "+str(cliente))
    print("--------------------------------")
    total=0
    for i, p in enumerate(pedido,1):
        print(f"{i}. {p.get_nombre()} - ${p.get_precio()}")
        total += p.get_precio()
    print(f"\nTotal hasta el momento: ${total}")
    
    input("\nPresione Enter para continuar...")

    
def nuevoPlatilloMenu():
    id=len(Platillos)+1
    nombre=val.Str("Nombre del Nuevo Platillo: ")
    precio=val.intPositivos("Precio: ")
    dispo="Disponible"
    
    nuevo= Platillo(id,nombre,precio,dispo)
    Platillos.append(nuevo)
    print("Platillo Agregado correctamente al Menu")
    input("Presione Enter para continuar...")

def cambiarDis():
    mostrarmenu()
    print("\nPara modificar la disponibilidad el platillo,")
    id=int(val.intPositivos("Ingrese el numero del platillo:"))
    
    for p in Platillos:
        if p.get_platilloID()==id:
            if p.get_disponibilidad()=="Disponible":
                p.set_disponibilidad("No Disponible")
            else:
                p.set_disponibilidad("Disponible")
            print("Disponibilidad Actualizada")
            input("\nPresione Enter para continuar...")
            return
            
def CancelarPedido():
    pedido.clear()
    print("PEDIDO CANCELADO. NO SE CONTINUARA")
    input("Seleccione Enter para Salir...")
    
def finalizarPedido():
    if not pedido:
        print("No hay platillos en el pedido")
        return
    total =0
    print("\n--- PRECESO DE FINALIZACION ---")
    print("PEDIDO DE: "+ str(cliente))
    print("--------------------------------")
    for p in pedido:
        print(f"{p.get_nombre()} - ${p.get_precio()}")
        total+=p.get_precio()

    print(f"\nTotal a Pagar: ${total}")
    pedido.clear()  
    input("Presione Enter para finalizar...")
    
def eliminarPla():
    if not pedido:
        print("No hay platillos para Eliminar")
        return
    mostrarPedido()
    id= val.intPositivos("Seleccione el Platillo a Eliminar: ")
    if 1 <= id <= len(pedido):
        eliminado = pedido.pop(id-1)
        print(f"{eliminado.get_nombre()} eliminado del pedido")
    else:
        print("Opción inválida")
    