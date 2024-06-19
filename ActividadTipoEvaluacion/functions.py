import os


def clearConsole():
    os.system("cls")


def showMenu():
    print("1) Registrar Estudiante")
    print("2) Buscar Estudiante")
    print("3) Imprimir Certificados ")
    print("4) Salir")


def agregarId():
    while True:
        idIngresado = input("ingrese ID de alumno\n").lower()
        while not idIngresado:
            idIngresado = input("ID no puede estar vacio\n")
        if idIngresado.endswith("-ab") or idIngresado.endswith("-am"):
            print("id weno")
            return idIngresado
        else:
            print("ID invalido")


def agregarNombre():
    while True:
        nombreIngresado = input("ingrese nombre de alumno\n").lower()
        while not nombreIngresado:
            nombreIngresado = input("Nombre no puede estar vacio\n")
        if len(nombreIngresado) >= 5:
            print("nombre weno")
            return nombreIngresado
        else:
            print("nombre invalido")


def agregarEdad():
    while True:
        # verificando que valor no venga vacio
        edadS = input("ingrese edad estudiante")
        while not edadS:
            edadS = input("ingrese edad estudiante, no debe venir vacio")
        try:
            edadIngresada = int(edadS)
            # confirmando que valor cumpla requisitos
            while edadIngresada >= 12 or edadIngresada <= 18:
                return edadIngresada
        except:
            print("para el campo edad, solo se permiten valores de tipo numerico")


def registarEstudiante():
    id = agregarId()
    nombre = agregarNombre()
    edad = agregarEdad()
