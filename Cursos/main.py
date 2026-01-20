import datos
import val
import funciones
opcM=-1
val.limpiar_consola()
while opcM!=0:
    print("\nM E N U  P R I N C I P A L ")
    print("1.- INSCRIPCIÓN A CURSO")
    print("2.- BAJA DE ALUMNO EN UN CURSO")
    print("3.- CONSULTA DE CUPO")
    print("0.- SALIR")
    
    opcM= int(input("Opcion: "))
    
    match opcM:
        case 1:
            val.limpiar_consola()
            funciones.inscribirAlumno()
        case 2:
            val.limpiar_consola()
            funciones.bajaAlumno()
        case 3:
            val.limpiar_consola()
            funciones.consultaCupoCurso()
            
        case 0:
            break
        case _:
            print("OPCION INVALIDA.")