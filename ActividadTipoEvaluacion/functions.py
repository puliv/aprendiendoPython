import os

estudiantes = [
    {"id": "00-AM", "nombre": "nombre1", "edad": 33},
    {"id": "01-AM", "nombre": "nombre2", "edad": 23},
]


def limpiarTerminal():
    os.system("cls")


def mostrarMenu():
    print("1) Registrar Estudiante")
    print("2) Buscar Estudiante")
    print("3) Imprimir Certificados")
    print("4) Eliminar Estudiante ")
    print("5) Salir")


def agregarId(contadorIds):
    grado = input("Ingrese grado academico: basica o media\n").lower()
    while grado not in ["basica", "media"]:
        grado = input("ingrese grado academico: basica o media\n").lower()
    if grado == "basica":
        sufijo = "AB"
    elif grado == "media":
        sufijo = "AM"
    # Contador para designar un numero correlativo a cada estudiante ingresado
    idinal = "0" + str(contadorIds) + "-" + sufijo
    contadorIds += 1
    return idinal


def agregarNombre():
    while True:
        nombreIngresado = input("Ingrese nombre de alumno\n").lower()
        while not nombreIngresado:
            nombreIngresado = input("Nombre no puede estar vacio\n")
        if len(nombreIngresado) >= 5:
            return nombreIngresado
        else:
            print("Nombre invalido")


def agregarEdad():
    while True:
        # verificando que valor no venga vacio
        edadS = input("ingrese edad estudiante\n")
        while not edadS:
            edadS = input("ingrese edad valida, no debe estar vacio\n")
        try:
            edadIngresada = int(edadS)
            # confirmando que valor cumpla requisitos
            while edadIngresada >= 12 or edadIngresada <= 18:
                return edadIngresada
        except:
            print("para el campo edad, solo se permiten valores de tipo numerico")


def registrarEstudiante():
    contadorIds = 1
    while True:
        idEstudiante = agregarId(contadorIds)
        contadorIds += 1
        nombre = agregarNombre()
        edad = agregarEdad()
        estudiante = {"id": idEstudiante, "nombre": nombre, "edad": edad}
        estudiantes.append(estudiante)
        print(estudiantes)
        input("...")

        try:
            agregar_estudiante = input(
                "Quieres agregar otro estudiante? Si  No\n"
            ).lower()
            while not agregar_estudiante:
                agregar_estudiante = input(
                    "Quieres agregar otro estudiante? No debe venir vacio\n"
                ).lower()
            while agregar_estudiante not in ["si", "no"]:
                agregar_estudiante = input(
                    "Quieres agregar otro estudiante? Escribe Si o No\n"
                ).lower()
            if agregar_estudiante == "si":
                continue
            else:
                break
        except:
            print("solo acepta como opcion si  y no")


def buscarEstudiante():
    idIngresado = input("Ingrese id de estudiante\n").upper()
    while not idIngresado:
        idIngresado = input("Ingrese id de estudiante, no puede estar vacio\n").upper()
    if idIngresado.endswith("-AM") or idIngresado.endswith("-AB"):
        for est in estudiantes:
            print("ends", est)
            if est.id == idIngresado:
                print(est)
                input("...")
    else:
        idIngresado = input("Ingrese id de estudiante valido\n")
