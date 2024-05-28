import os, time

menuAbierto = True
rutIncorrecto = True
edadIncorrecta = True

while menuAbierto:
    print("**********Centro Médico DUOC**********")
    print("1) Registrar Paciente")
    print("2) Atención Paciente")
    print("3) Gestionar Paciente")
    print("4) Salir")
    try:
        opcion = int(input("Ingrese opcion"))
        if opcion == 1:
            os.symtem("cls")
            print("**********Registrar Paciente**********")
            while rutIncorrecto:
                try:
                    rut = int(input("Ingrese rut paciente"))
                    if rut < 5000000 or rut > 99999999:
                        print("Ingrese rut valido")
                    else:
                        print("Rut ingresado")
                        rutIncorrecto = False
                except:
                    print("Rut solo acepta numeros")
            while edadIncorrecta:
                try:
                    edad = int(input("Ingrese Edad paciente"))
                    if edad < 0 or edad > 110:
                        print("Ingrese Edad valida")
                    else:
                        print("Edad ingresada")
                        edadIncorrecta = False
                except:
                    print("Edad solo acepta numeros")
            genero = input("Ingrese F o M para género del paciente segun corresponda")
        elif opcion == 2:
            print("**********Atención Paciente**********")
        elif opcion == 3:
            print("**********Gestionar Paciente**********")
        elif opcion == 4:
            print("**********Salir**********")
        else:
            print("opcion no existe")
    except:
        print("Ingrese solo numeros")
