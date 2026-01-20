# algo

import mCarrito 

opc = -1
while opc != 0:
    print("---CARRITO DE COMPRAS---")
    print("\n1. Agregar producto \n2. Eliminar producto \n3. Consultar Carrito \n4. Vaciar carrito \n0. Salir\n")
    opc = int(input("Opcion: "))
    match opc:
        case 1:
            mCarrito.Agregar()
            
        case 2:
            mCarrito.Eliminar()
            
        case 3:
            mCarrito.Consultar()
            
        case 4:
            mCarrito.Vaciar()
            
        case 0:
            print("Saliendo...")