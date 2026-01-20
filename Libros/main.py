#LAS IDENTIDADES SE CREARAN EN CLASES, POR EJEMPLO LIBRO SERA MI CLASE, USUARIO TAMBIEN SERA OTRA CLASE, 
#POR CADA CLASE SE TIENEN METODOS, LOS ATRIBUTOS SERAN LOS QUE ESPEFICICA EL TEXTO
#LOS METODOS SERAN LAS OPERACIONES QUE SE DEBEN DE REALIZAR
import storage
import val
import funciones
opcM=-1
val.limpiar_consola()
while opcM!=0:
    print("\nM E N U  P R I N C I P A L ")
    print("1.- RESERVAR UN LIBRO")
    print("2.- CONSULTAR DISPONIBILIDAD")
    print("3.- CANCELAR RESERVACIÓN")
    print("0.- SALIR")
    
    opcM= int(input("Opcion: "))
    
    match opcM:
        case 1:
            val.limpiar_consola()
            funciones.reservarLib()
        case 2:
            funciones.consutaLibro()
        case 3:
            funciones.cancelarReserva()
        case 4:
            funciones.verLibros()
        case 5:
            val.limpiar_consola()
            storage.verLibros()
        case 0:
            break
        case _:
            print("OPCION INVALIDA.")