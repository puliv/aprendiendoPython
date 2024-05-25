# registros = int(input("7) Registros"))

import os, time

rutIncorrecto = True
edadIncorrecta = True
previsionIncorrecta = True
rutPacienteIncorrecto = True
menuAbierto = True

while menuAbierto:
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
            nombre = input("Ingrese nombre\n")
            while nombre == "":
                nombre = input("Ingrese nombre válido\n")

            gender = input(
                "Ingrese genero, (solo acepta como caracteres las letras f o m)\n"
            )
            while gender not in "fmFM":
                gender = input("Ingrese f o m segun corresponda\n")

            dirección = input("Ingrese dirección\n")
            while dirección == "":
                dirección = input("Ingrese dirección válida\n")

            while rutIncorrecto:
                try:
                    rut = int(input("Ingrese Rut, sin dígito verificador ni puntos.\n"))
                    while rut < 5000000 or rut > 99999999:
                        rut = int(input("Ingrese Rut válido\n"))
                    rutIncorrecto = False
                except:
                    print("Solo se permiten números para el Rut")

            correo = input("Ingrese Correo\n")
            while "@" not in correo:
                correo = input("Ingrese correo válido\n")

            while edadIncorrecta:
                # con el try y except estamos asegurandonos que los datos
                # que pedimos sean numeros, no caracteres
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
                    previsionIncorrecta = False
                except:
                    print("Solo se admite el numero 1 para Isapre y 2 para Fonasa")
            time.sleep(1)
            print("******Paciente registrado con exito******")
            next = input("Presione enter para continuar\n")
        elif opcion == 2:
            os.system("cls")
            print("******Atención Paciente******")
            while rutPacienteIncorrecto:
                try:
                    rutPaciente = int(input("Ingrese rut paciente"))
                    if rutPaciente == rut:
                        print("******Paciente verificado******")
                        registro = input(
                            "Ingrese fecha (dd/mm/aaa) y observaciones del paciente"
                        )
                        rutPacienteIncorrecto = False
                    else:
                        print("rut ingresado no existe en la ficha")
                except:
                    print("Solo acepta numeros")
        elif opcion == 3:
            rutIncorrecto = True
            os.system("cls")
            print("******Consultar Datos Paciente******")
            while rutPacienteIncorrecto:
                try:
                    rutPaciente = int(input("Ingrese rut paciente\n"))
                    if rutPaciente == rut:
                        print("******Paciente verificado******")
                        print(
                            'nombre: "{nombre}"\ndirección: "{dirección}"\nrut: "{rut}"\ncorreo: "{correo}"\nedad: "{edad}"\nprevision: "{prevision}"\nregistro: "{registro}"'
                        )
                        rutPacienteIncorrecto = False
                    else:
                        print("rut ingresado no existe en la ficha")
                except:
                    print("Solo acepta numeros")
        elif opcion == 4:
            os.system("cls")
            print("****************************")
            print("***Has salido del sistema***")
            print("****************************")
            menuAbierto = False
        else:
            print("Opcion incorrecta")
    except:
        print("El sistema solo admite numeros para seleccionar un item del menu")
