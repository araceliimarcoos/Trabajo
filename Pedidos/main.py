import menu
import val
import mPedido
while True:
    
    menu.menuPrincipal()
    opc=int(val.intPositivos("\nSeleccione una opcion:"))
    match opc:
        case 1:
            val.limpiar()
            mPedido.mostrarmenu()
            input("Presione Enter para Regresar...")
        case 2:
            val.limpiar()
            mPedido.pedido.clear()
            mPedido.cliente=val.Str("¿A Nombre de quien sera el pedido?")
            while True:
                val.limpiar()
                menu.menu()
                opc1=int(val.intPositivos("\nSeleccione una opcion:"))
                match opc1:
                    case 1:
                        val.limpiar()
                        mPedido.mostrarPedido()
                    case 2:
                        val.limpiar()
                        mPedido.agregarPlatillo()
                    case 3:
                        val.limpiar()
                        mPedido.eliminarPla()
                    case 4:
                        val.limpiar()
                        mPedido.finalizarPedido()
                        break
                    case 5:
                        val.limpiar()
                        mPedido.CancelarPedido()
                        break
                        
                    case 0:
                        break
                                
        case 3:
            val.limpiar()
            while True:
                menu.adminMenu()
                opc2=int(val.intPositivos("\nSeleccione una opcion:"))
                match opc2:
                    case 1:
                        val.limpiar()
                        mPedido.nuevoPlatilloMenu()
                        
                    case 2:
                        val.limpiar()
                        mPedido.cambiarDis()
                    case 3:
                        val.limpiar()
                        mPedido.mostrarmenu()
                    case 0:
                        break
        case 0:
            break
                
        