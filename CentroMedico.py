
# registros = int(input("7) Registros"))

import os, time

rutIncorrecto = True
edadIncorrecta = True
previsionIncorrecta = True

while True:
    os.system("cls")
    print("1) Registrar Paciente")
    print("2) Atención Paciente")
    print("3) Consultar Datos Paciente")
    print("4) Salir")
    try:
        opcion = int(input("Ingrese opcion\n"))
        if opcion == 1:
            os.system("cls")
            print("******Registrar Paciente******")

            nombre= int(input("Ingrese nombre\n"))
            while nombre == "":
                nombre= int(input("Ingrese nombre válido\n"))

            gender = input(
                "Ingrese genero, solo puede aceptar como caracteres las letras f o m\n"
            )
            while gender not in "fmFM":
                gender = input("Ingrese f o m segun corresponda\n")

            dirección= int(input("Ingrese dirección\n"))
            while dirección == "":
                dirección= int(input("Ingrese dirección válida\n"))

            while rutIncorrecto:
                try:
                    rut = int(input("Ingrese Rut, sin dígito verificador ni puntos.\n"))
                    while rut < 5000000 or rut > 99999999:
                        rut = int(input("Ingrese Rut válido\n"))
                    rutIncorrecto = False
                except:
                    print(
                        "Solo se permiten números para el Rut, sin dígito verificador ni puntos"
                    )

            correo = input("Ingrese Correo\n")
            while correo == "" or "@" not in correo:
                correo = input("Ingrese Correo válido\n")

            while edadIncorrecta:
                try:
                    edad = int(input("Ingrese Edad\n"))
                    while edad < 18 or edad > 110:
                        edad = int(input("Ingrese edad válida\n"))
                    edadIncorrecta = False
                except:
                    print("Edad solo acepta números")

            while previsionIncorrecta:
                try:
                    prevision = int(
                        input("Ingrese prevision de salud: 1)Isapre  2)Fonasa\n")
                    )
                    while prevision < 1 or prevision > 2:
                        prevision = int(
                            input("Ingrese Prevision Salud válida 1)Isapre  2)Fonasa\n")
                        )
                except:
                    print("Solo se admite el numero 1 para Isapre y 2 para Fonasa")
            
        elif opcion == 2:
            os.system("cls")
            print("******Atención Paciente******")
        elif opcion == 3:
            os.system("cls")
            print("******Consultar Datos Paciente******")
        elif opcion == 4:
            os.system("cls")
            print("Has salido del sistema")
        else:
            print("Opcion incorrecta")
    except:
        print("El sistema solo admite numeros para seleccionar un item del menu")
