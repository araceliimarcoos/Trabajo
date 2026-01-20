from libros import Libros
from storage import listaLibros
import val


def reservarLib():
    val.limpiar_consola()
    print("R E S E R V A R  U N  L I B R O")

    while True:
        id = int(input("Ingrese el ID del libro para reservar: "))
        libroEnc = False

        for libros in listaLibros:
            if libros.get_id() == id:
                libroEnc = True
                #val.limpiar_consola()

                print("Datos del libro")
                print(f"Titulo : {libros.get_titulo()}")
                print(f"Autor  : {libros.get_autor()}")
                print(f"Estado : {libros.get_estado()}")

                while True:
                    print("\n¿Es el libro correcto?")
                    print("(S) Sí")
                    print("(N) No")
                    opcion = val.vSioNo("Seleccione una opción: ")

                    if opcion == "S":
                        if libros.get_estado() == "Reservado":
                            val.limpiar_consola()
                            print("Este libro ya se encuentra reservado.")
                            input("Presione Enter para regresar")
                            return

                        elif libros.get_estado() == "Disponible":
                            print("\nEl libro se encuentra disponible.")
                            print("¿Estás seguro de reservarlo?")
                            print("(S) Sí")
                            print("(N) No")
                            opcion = val.vSioNo("Seleccione una opción: ")

                            if opcion == "S":
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

        if not libroEnc:
            val.limpiar_consola()
            print("No se ha encontrado el libro.")
            input("Presione Enter para intentar de nuevo")
            
            
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

def cancelarReserva():
    val.limpiar_consola()
    print("C A N C E L A R  R E S E R V A")

    id = int(input("Ingrese el ID del libro a cancelar la reserva: "))
    libroEnc = False

    for libros in listaLibros:
        if libros.get_id() == id:
            libroEnc = True
            val.limpiar_consola()

            print("Datos del libro")
            print(f"Titulo : {libros.get_titulo()}")
            print(f"Autor  : {libros.get_autor()}")
            print(f"Estado : {libros.get_estado()}")

            if libros.get_estado() == "Disponible":
                print("\nEste libro no tiene una reserva activa.")
                input("Presione Enter para continuar")
                val.limpiar_consola()
                return

            print("\n¿Desea cancelar la reserva de este libro?")
            print("(S) Sí")
            print("(N) No")
            opcion = val.vSioNo("Seleccione una opción: ")

            if opcion == "S":
                libros.set_estado("Disponible")
                val.limpiar_consola()
                print("La reserva ha sido cancelada correctamente.")
                input("Presione Enter para continuar")
                val.limpiar_consola()
                return
            else:
                val.limpiar_consola()
                print("Operación cancelada.")
                input("Presione Enter para regresar")
                val.limpiar_consola()
                return

    if not libroEnc:
        val.limpiar_consola()
        print("No se ha encontrado el libro.")
        input("Presione Enter para intentar de nuevo")
        val.limpiar_consola()


def verLibros():
    val.limpiar_consola()
    print("\nL I S T A  D E  L I B R O S\n")

    for libro in listaLibros:
        print(libro)

    input("\nPresione Enter para continuar")
    val.limpiar_consola()
