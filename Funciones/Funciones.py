def verMenuFunc():
    print("1) Registrar Paciente")
    print("2) Atencion Paciente")
    print("3) Gestionar Paciente")
    print("4) Salir")


def validarRut(rutS):
    while rutS < 5000000 or rutS > 30000000:
        rut = int(input("ingrese rut, debe estar en rango 5M Y 30M\n"))
    return rut


def validarEdad(num):
    while num < 0 or num > 110:
        edad = int(input("ingrese edad, entre 0 110\n"))
    return edad
