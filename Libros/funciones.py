from libros import Libros
from storage import listaLibros
import val

####################################################################################################
def reservarLib():
    val.limpiar_consola()
    print("R E S E R V A R  U N  L I B R O")

    while True:
        id = int(input("Ingrese el ID del libro para reservar: "))
        libroEnc = False #Se inicializa en falso 

        for libros in listaLibros: #Se recorre la lista de libros para ver si el ID existe
            if libros.get_id() == id:
                libroEnc = True
                #val.limpiar_consola()

                print("Datos del libro") #Aqui se muestran los datos del libro encontrado
                print(f"Titulo : {libros.get_titulo()}")
                print(f"Autor  : {libros.get_autor()}")
                print(f"Estado : {libros.get_estado()}")

                while True: #Se pregunta al usuario si es el libro correcto
                    print("\n¿Es el libro correcto?")
                    print("(S) Sí")
                    print("(N) No")
                    opcion = val.vSioNo("Seleccione una opción: ")

                    if opcion == "S": #Si es el libro correcto, se verifica su estado por si ya esta reservado
                        if libros.get_estado() == "Reservado": #Si ya esta reservado
                            val.limpiar_consola()
                            print("Este libro ya se encuentra reservado.")
                            input("Presione Enter para regresar")
                            return

                        elif libros.get_estado() == "Disponible": #Si el libro esta disponible
                            print("\nEl libro se encuentra disponible.")
                            print("¿Estás seguro de reservarlo?")
                            print("(S) Sí")
                            print("(N) No")
                            opcion = val.vSioNo("Seleccione una opción: ")

                            if opcion == "S": #Preguntamos si esta seguro de reservar el libro
                                libros.set_estado("Reservado")
                                val.limpiar_consola()
                                print("El libro ha sido reservado.")
                                input("Presione Enter para continuar")
                                return
                            else:
                                val.limpiar_consola()
                                print("Operación cancelada.")
                                input("Presione Enter para regresar")
                                return

                    elif opcion == "N":
                        val.limpiar_consola()
                        print("Regresando al menú...")
                        return

        if not libroEnc: #Si no se encuentra el libro con el ID ingresado
            val.limpiar_consola()
            print("No se ha encontrado el libro.")
            input("Presione Enter para intentar de nuevo")
            
####################################################################################################################
def consultaLibro():
    val.limpiar_consola()
    id = int(input("Ingrese el ID del libro a consultar: "))
    libroEnc = False

    for libros in listaLibros:
        if libros.get_id() == id:
            libroEnc = True
            val.limpiar_consola()

            print("Datos del libro")
            print(f"Titulo : {libros.get_titulo()}")
            print(f"Autor  : {libros.get_autor()}")
            print(f"Estado : {libros.get_estado()}")

            input("\nPresione Enter para continuar")
            val.limpiar_consola()
            return

    if not libroEnc:
        val.limpiar_consola()
        print("No se ha encontrado el libro.")
        input("Presione Enter para intentar de nuevo")
        val.limpiar_consola()
        
##################################################################################################################
def cancelarReserva():
    val.limpiar_consola()
    print("C A N C E L A R  R E S E R V A")

    id = int(input("Ingrese el ID del libro a cancelar la reserva: "))
    libroEnc = False #Empezamos en false

    for libros in listaLibros: #Empieza a recorrer la lista de libros
        if libros.get_id() == id: #Aki si si existe
            libroEnc = True
            val.limpiar_consola()

            print("Datos del libro") #Mostramos los datos
            print(f"Titulo : {libros.get_titulo()}")
            print(f"Autor  : {libros.get_autor()}")
            print(f"Estado : {libros.get_estado()}")

            if libros.get_estado() == "Disponible": #Comparamos su disponibilidad | Disponible
                print("\nEste libro no tiene una reserva activa.")
                input("Presione Enter para continuar")
                val.limpiar_consola()
                return

            elif libros.get_estado() == "Reservado": #Comparamos su disponibilidad | Reservado
                print("\n¿Desea cancelar la reserva de este libro?")
                print("(S) Sí")
                print("(N) No")
                opcion = val.vSioNo("Seleccione una opción: ")

                if opcion == "S":
                    libros.set_estado("Disponible")
                    val.limpiar_consola()
                    print("La reserva ha sido cancelada correctamente.")
                else:
                    val.limpiar_consola()
                    print("Operación cancelada.")

                input("Presione Enter para continuar")
                val.limpiar_consola()
                return
    if not libroEnc:
        val.limpiar_consola()
        print("No se ha encontrado el libro.")
        input("Presione Enter para intentar de nuevo")
        val.limpiar_consola()
        
###############################################################################################################################
def verLibros():
    val.limpiar_consola()
    print("\nL I S T A  D E  L I B R O S\n")

    for libro in listaLibros:
        print(libro)

    input("\nPresione Enter para continuar")
    val.limpiar_consola()

