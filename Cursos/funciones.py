import val
from datos import listaCursos, listaAlumnos
#########################################################################################################################
def inscribirAlumno():
    print("I N S C R I B I R  A L U M N O")

    idCurso = int(input("Ingrese la clave del curso: "))
    cursoEnc = False

    for curso in listaCursos:
        if curso.get_clave() == idCurso:
            cursoEnc = True #De q si se encontro el id del curso
            val.limpiar_consola()

            print("Datos del curso") #Nomas para se imprima chido
            print(f"Clave       : {curso.get_clave()}")
            print(f"Nombre      : {curso.get_nombre()}")
            print(f"Cupo máximo : {curso.get_maxAlumnos()}")
            print(f"Inscritos   : {len(curso.get_alumnos())}") #Aqui se mide cuantos alumnos hay inscritos con len()

            if len(curso.get_alumnos()) >= curso.get_maxAlumnos(): #Medir que el cupo de alumnos no se exceda
                print("\nEl curso ya no tiene cupo disponible.")
                input("Presione Enter para continuar")
                val.limpiar_consola()
                return

            idAlumno = int(input("\nIngrese el ID del alumno: ")) #ID del alumno
            alumnoEnc = False

            for alumno in listaAlumnos:
                if alumno[0] == idAlumno:
                    alumnoEnc = True #De q el alumno si existe

                    # Se revisa que el alumno no este ya inscrito
                    if alumno in curso.get_alumnos():
                        print("\nEste alumno ya está inscrito en el curso.")
                        input("Presione Enter para continuar")
                        val.limpiar_consola()
                        return

                    print("\nDatos del alumno") #Para q los datos se impriman chido
                    print(f"ID     : {alumno[0]}")
                    print(f"Nombre : {alumno[1]}")

                    print("\n¿Desea inscribir a este alumno?") #Preguntamos para corroborar
                    print("(S) Sí")
                    print("(N) No")
                    opcion = val.vSioNo("Seleccione una opción: ")

                    if opcion == "S": #Aqui ya lo inscribimos bien
                        curso.get_alumnos().append(alumno)
                        val.limpiar_consola()
                        print("Alumno inscrito correctamente.")
                        input("Presione Enter para continuar")
                        val.limpiar_consola()
                        return
                    else: #Aqui por si dice q no
                        val.limpiar_consola()
                        print("Inscripción cancelada.")
                        input("Presione Enter para regresar")
                        val.limpiar_consola()
                        return

            if not alumnoEnc: #Aqui de que no se encontro su ID (del alumno)
                val.limpiar_consola()
                print("No se ha encontrado el alumno.")
                input("Presione Enter para intentar de nuevo")
                val.limpiar_consola()
                return

    if not cursoEnc: #Aqui de que no se encontro el curso
        val.limpiar_consola()
        print("No se ha encontrado el curso.")
        input("Presione Enter para intentar de nuevo")
        val.limpiar_consola()
        
##########################################################################################################################
def bajaAlumno():
    print("B A J A  D E  A L U M N O")

    idCurso = int(input("Ingrese la clave del curso: ")) #Se ingresa el ID del curso
    cursoEnc = False #Se fija en falso para despues ver si se encontro

    for curso in listaCursos: #Aqui se busca el curso dentro del for
        if curso.get_clave() == idCurso:
            cursoEnc = True #De q si se encontro el curso
            val.limpiar_consola()

            print("Datos del curso") #Solo para q se imprima chido
            print(f"Clave       : {curso.get_clave()}")
            print(f"Nombre      : {curso.get_nombre()}")
            print(f"Inscritos   : {len(curso.get_alumnos())}") #Aqui se mide cuantos alumnos hay inscritos con len()

            if len(curso.get_alumnos()) == 0: #Si no hay ningn alumno inscrito
                print("\nEste curso no tiene alumnos inscritos.")
                input("Presione Enter para continuar")
                val.limpiar_consola()
                return

            idAlumno = int(input("\nIngrese el ID del alumno a dar de baja: "))
            alumnoEnc = False #Fijar en falso para despues ver si se encontro

            for alumno in curso.get_alumnos(): #Empiezas a buscar al alumno en el curso
                if alumno[0] == idAlumno: #Si se encuentra el ID del alumno
                    alumnoEnc = True#Se encontro

                    print("\nDatos del alumno")
                    print(f"ID     : {alumno[0]}")
                    print(f"Nombre : {alumno[1]}")

                    print("\n¿Desea dar de baja a este alumno?")
                    print("(S) Sí")
                    print("(N) No")
                    opcion = val.vSioNo("Seleccione una opción: ")

                    if opcion == "S":
                        curso.get_alumnos().remove(alumno) #Aqui se da de baja al alumno
                        val.limpiar_consola()
                        print("Alumno dado de baja correctamente.")
                        input("Presione Enter para continuar")
                        val.limpiar_consola()
                        return
                    else:
                        val.limpiar_consola()
                        print("Operación cancelada.") # Al final no se dio de baja
                        input("Presione Enter para regresar")
                        val.limpiar_consola()
                        return

            if not alumnoEnc:
                val.limpiar_consola()
                print("El alumno no está inscrito en este curso.")#No se encontro al alumno
                input("Presione Enter para intentar de nuevo")
                val.limpiar_consola()
                return

    if not cursoEnc: #Por si no se encontro el curso
        val.limpiar_consola()
        print("No se ha encontrado el curso.")
        input("Presione Enter para intentar de nuevo")
        val.limpiar_consola()

##########################################################################################################################################

def consultaCupoCurso():
    val.limpiar_consola()
    print("C O N S U L T A  D E  C U P O  D E L  C U R S O")

    idCurso = int(input("Ingrese la clave del curso: "))
    cursoEnc = False#Se fija en falso 

    for curso in listaCursos: #Busca el curso
        if curso.get_clave() == idCurso: #Aqui si se encontro
            cursoEnc = True
            val.limpiar_consola()

            inscritos = len(curso.get_alumnos()) #Mide la cantidad de alumnos inscritos
            maximo = curso.get_maxAlumnos() #Este esta en la clase curso
            disponibles = maximo - inscritos #Varible q definimos para ver cuantos cupos quedan

            print("Datos del curso")
            print(f"Clave           : {curso.get_clave()}")
            print(f"Nombre          : {curso.get_nombre()}")
            print(f"Cupo máximo     : {maximo}")
            print(f"Alumnos inscritos: {inscritos}")
            print(f"Cupo disponible : {disponibles}")

            input("\nPresione Enter para continuar")
            val.limpiar_consola()
            return

    if not cursoEnc:
        val.limpiar_consola()
        print("No se ha encontrado el curso.") #Por si no se encontro el curso
        input("Presione Enter para intentar de nuevo")
        val.limpiar_consola()
