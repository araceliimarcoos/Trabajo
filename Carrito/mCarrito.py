# Metodos del carrito de compras

from producto import producto
from Datos import productos_disponibles
import val

carrito = {} # Esto es un diccionario anidado, dentro tiene el id y 

def MostrarProductos():
    print("\nProductos:") 
    for p in productos_disponibles:
        if p.get_status() == "si":
            print(f"ID: {p.get_id()} - {p.get_name()} - ${p.get_price()}")    

def Agregar():
    print("\n---AGREGAR PRODUCTOS---") # y ahora q?
    MostrarProductos()
    
    id = val.intPositivos("\nIngrese el ID del producto: ")
    
    Prod_encontrado = None
    for p in productos_disponibles:
        if p.get_id() == id and p.get_status() == "si": # le faltan modificaciones. weno ya no
            Prod_encontrado = p
            break
        
    if Prod_encontrado:
        cantidad = val.intPositivos(f"\nCantidad de {Prod_encontrado.get_name()} deseada: ")

        if cantidad > 0:
            if id in carrito:
                carrito[id]["cantidad"] += cantidad
            else:
                carrito[id] = {"producto": Prod_encontrado, "cantidad":cantidad}
            print(f"Añadido: {Prod_encontrado.get_name()} x {cantidad}")
            input(" Presione Enter para continuar...")
            val.limpiar_consola()
    else:
        print("Producto no disponible")
        input(" Presione Enter para continuar...")
        val.limpiar_consola()
        
def Eliminar():
    print("\n---ELIMINAR PRODUCTOS---")
    
    for i in carrito.values():
        prod = i["producto"]
        cantidad = i["cantidad"]
        print(f"ID: {prod.get_id()} - {prod.get_name()} - ${prod.get_price()} x {cantidad}")
    
    id = val.intPositivos("Ingrese el ID del producto a eliminar: ")
    
    #verificar existencia
    if id in carrito:
        Cantidad_eliminar = val.intPositivos(f"\nCantidad de {carrito[id]["producto"].get_name()} a eliminar: ") # creo q ya le voy agarrando la onda
        if Cantidad_eliminar < carrito[id]["cantidad"]:
            carrito[id]["cantidad"] -= Cantidad_eliminar
            print(f"Eliminado: {carrito[id]["producto"].get_name()} x {Cantidad_eliminar}")
            input(" Presione Enter para continuar...")
            val.limpiar_consola()
        else:
            carrito[id]["cantidad"] = 0
            print(f"Eliminado: {carrito[id]['producto'].get_name()} x {Cantidad_eliminar}")
            del carrito[id]
            input(" Presione Enter para continuar...")
            val.limpiar_consola()
    else:
        print("Producto no encontrado")
        input(" Presione Enter para continuar...")
        val.limpiar_consola()
        
def Consultar():
    print("\n---DESGLOCE DE COMPRA---")
    total = 0
    for i in carrito.values():
        prod = i["producto"]
        cantidad = i["cantidad"]
        subtotal = prod.get_price() * cantidad
        total += subtotal
        print(f"{prod.get_name()} x {cantidad} - Subtotal: ${subtotal:.2f}")
    if total == 0:
        print("Carrito vacio")
    print(f"Total: ${total:.2f}")
    input(" Presione Enter para continuar...")
    val.limpiar_consola()
    
def Vaciar():
    confirmar = val.vSioNo("Desea vaciar el carrito? (S/N): ")
    if carrito == {}:
        print("El carrito ya esta vacio")
        input(" Presione Enter para continuar...")
        val.limpiar_consola()
    elif confirmar == "S":
        carrito.clear()
        print("Carrito vaciado")
        input(" Presione Enter para continuar...")
        val.limpiar_consola()
    else:
        print("Operación cancelada")
        input(" Presione Enter para continuar...")
        val.limpiar_consola()
        
