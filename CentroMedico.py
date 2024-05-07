# nombre= int(input("2) Nombre"))
# dirección= int(input("3) Dirección"))
import os, time

edadIncorrecta = True
while True:
    os.system("cls")
    print("1) Registrar Paciente")
    print("2) Atención Paciente")
    print("3) Consultar Datos Paciente")
    print("4) Salir")
    try:
        opcion = int(input("Ingresa opcion\n"))
        if opcion == 1:
            print("******Registrar Paciente******")
            rut = int(input("1)Ingrese Rut, sin dígito verificador ni puntos.\n"))
            while rut < 5000000 or rut > 99999999:
                rut = int(input("Ingrese Rut válido\n"))

            correo = input("4)Ingrese Correo\n")
            while correo == "" or "@" not in correo:
                correo = input("Ingrese Correo válido\n")

            while edadIncorrecta:
                try:
                    edad = int(input("5)Ingrese Edad\n"))
                    while edad < 18 or edad > 110:
                        edad = int(input("5) Ingrese edad válida\n"))
                    edadIncorrecta = False
                except:
                    print("Edad solo acepta números")

            sexo = int(
                input("6) Sexo, solo puede aceptar como caracteres las letras f o m")
            )
            registros = int(input("7) Registros"))
            prevision = int(input("7) Prevision Salud 1)Isapre  2)Fonasa"))

    except:
        print("Opcion incorrecta")
