import val
import Mcita
while True:
    val.limpiar_consola()
    print(" AGENDA DE CITAS ")
    print("\n   MENU   ")
    print("1.Agendar Cita \n2.Cancelar cita \n3.Consultar citas \n0.Salir")
    Opc= int(val.intPositivos("Seleccione una opcion: "))
    match Opc:
        case 1:
            val.limpiar_consola()
            Mcita.AgendarCita()
        case 2:
            val.limpiar_consola()
            print("CANCELAR CITA")
            Mcita.CancelarCita()
        case 3:
            val.limpiar_consola()
            print("CONSULTAR CITAS")
            Mcita.MostrarCitas()
        case 0:
            print("Saliendo...")
            break