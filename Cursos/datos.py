from cursos import Curso

listaCursos = [
    Curso(1, "Matemáticas", 30),
    Curso(2, "Programación", 3),
    Curso(3, "Base de Datos", 20),
    Curso(4, "Redes", 18),
    Curso(5, "Sistemas Operativos", 22),
    Curso(6, "Ingeniería de Software", 28),
    Curso(7, "Ética Profesional", 35),
    Curso(8, "Inteligencia Artificial", 15),
    Curso(9, "Desarrollo Web", 26),
    Curso(10, "Seguridad Informática", 20)
]

listaAlumnos = [
    (1, "Juan Pérez"),
    (2, "María López"),
    (3, "Carlos Hernández"),
    (4, "Ana García"),
    (5, "Luis Martínez"),
    (6, "Fernanda Rodríguez"),
    (7, "José Ramírez"),
    (8, "Daniela Cruz"),
    (9, "Miguel Torres"),
    (10, "Sofía Morales")
]

#Append hace que se agreguen alumnos a los cursos , es decir, agrega datos a los arrays ya hechos
#Curso1
listaCursos[0].get_alumnos().append(listaAlumnos[0])  # Juan Pérez
listaCursos[0].get_alumnos().append(listaAlumnos[1])  # María López

#Curso2
listaCursos[1].get_alumnos().append(listaAlumnos[2])  # Carlos Hernández
listaCursos[1].get_alumnos().append(listaAlumnos[1]) # Juan Pérez
listaCursos[1].get_alumnos().append(listaAlumnos[0]) #María López

#Curso3
listaCursos[2].get_alumnos().append(listaAlumnos[3])  # Ana García
listaCursos[2].get_alumnos().append(listaAlumnos[4])  # Luis Martínez
