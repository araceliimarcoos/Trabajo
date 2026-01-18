from Datos import citas
from Cita import Cita
import val
from tabulate import tabulate

numero=6
   
def AgendarCita():
    global numero
    while True:
        print("AGENDAR CITA")
        fecha = val.fecha("Ingrese la fecha. Use el formato DD/MM/YYYY: ")
        hora = val.hora("Ingrese la hora. Use formato HH:MM: ")
        c=ExisteCita(fecha, hora)
        if c==False:
            descripcion=val.Str("Descripcion: ")
            estado="Pendiente"
            NuevaCita = Cita(numero, fecha, hora, descripcion, estado)
            citas.append(NuevaCita)
            print("Cita Guardada Correctamente \nNumero de cita " + str(numero))
            input("presione enter para regresar")
            numero+=1 
            break
        else:
            r=input(" La fecha y hora no esta disonible \n Cualquier tecla para volver a intentar \n 0 para Salir \nOpcion:")
            if r=="0":
                break
            else:
                val.limpiar_consola() 
                
   

def CancelarCita():
    while True:
        id = val.intPositivos("Ingrese el numero de la cita: ")
        encontrado = False

        for cita in citas:
            if cita.get_numero() == id:
                encontrado = True
                if cita.get_estado() == "Hecha":
                    print("La cita ya se realizó")
                    input("Presione enter para regresar")
                elif cita.get_estado() == "Pendiente":
                    print("Datos de la Cita")
                    print(f"Numero Cita       : {cita.get_numero()}")
                    print(f"Fecha             : {cita.get_fecha()}")
                    print(f"Hora              : {cita.get_hora()}")
                    print(f"Descripcion       : {cita.get_descripcion()}")
                    print(f"Estado            : {cita.get_estado()}")
                    res = val.vSioNo("\nDesea cancelar esta cita? S/N: ")
                    if res == "S":
                        cita.set_estado("Cancelada")
                        print("Cita cancelada correctamente")
                        input("Presione enter para regresar")
                break  

        if encontrado==False:
            print("No se encontró ninguna cita con ese número.")
            input("Presione enter para intentar de nuevo")
        else:
            break  

            

def MostrarCitas():
    if not citas:
        print("No hay citas registradas")
    else:
        print("Numero  Fecha        Hora   Descripcion        Estado")
        print("-------------------------------------------------------")

        for c in citas:
            print(f"{c.get_numero():<7} {c.get_fecha():<12} {c.get_hora():<6} {c.get_descripcion():<18} {c.get_estado()}")
        input("Presione enter para regresar")

def ExisteCita(fecha, hora):
    for c in citas:
        if c.get_fecha() == fecha and c.get_hora() == hora:
            return True
    return False
