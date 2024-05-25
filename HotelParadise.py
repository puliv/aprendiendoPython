# Hotel "Paradise Dreams"
import os, time

numeroReserva = 0
nombreHuesped = ""
direccion = ""
correo = ""
edad = 0
numeroAcompanantes = 0
admin = None
passAdm = None
edadIncorrecta = True

while True:
    os.system("cls")
    print("*****Sistema de Gestión de Huéspedes******")
    print("1.- Registrar Huésped")
    print("2.- Consultar Datos Huésped")
    print("3.- Crear Usuario Admin")
    print("4.- Salir")
    try:
        opcion = int(input("Ingresa opción\n"))
        if opcion == 1:
            print("*****Registrar Huésped*****")
            time.sleep(1)
            numeroReserva = int(input("Ingresa Número de Reserva\n"))
            while numeroReserva < 1000 or numeroReserva > 9999:
                numeroReserva = int(input("Ingresa un número de reserva válido\n"))

            nombreHuesped = input("Ingresa Nombre del huésped\n")
            while nombreHuesped == "":
                nombreHuesped = input("Ingresa nombre del huésped\n")

            direccion = input("Ingresa dirección\n")
            while direccion == "":
                direccion = input("Ingresa dirección válida\n")

            correo = input("Correo electrónico\n")
            while "@" not in correo:
                correo = input("Correo electrónico\n")

            while edadIncorrecta:
                try:
                    edad = int(input("Edad\n"))
                    if edad < 18 and edad > 120:
                        edad = int(input("Ingresa edad entre 18 y 120 años\n"))
                    edadIncorrecta = False
                except:
                    print("edad solo acepta numeros")

            numeroAcompanantes = int(input("Número de acompañantes\n"))
            if numeroAcompanantes <= 0:
                numeroAcompanantes = int(input("Número de acompañantes debe ser minimo 1\n"))

            print("******Reserva creada con exito******")
            next = input("Presione enter para continuar\n\n")
        elif opcion == 2:
            print("*****Consulta Datos Huesped*****")
            time.sleep(1)

            adminUser = input("Ingrese nombre de usuario\n")
            while adminUser == "" or adminUser != admin:
                adminUser = input("Ingrese un nombre de usuario valido\n")

            adminPass = input("Ingrese contraseña de usuario\n")
            while adminPass == "" or adminPass != passAdm:
                adminPass = int(input("Ingrese contraseña de usuario válida\n"))

            print("*****Admin ingresado con exito*****")
            reservaIngresada = int(input("Ingresa numero de reserva\n"))
            while reservaIngresada < 1000 or reservaIngresada > 9999:
                reservaIngresada = int(input("Ingresa un numero de reserva válido\n"))
            if reservaIngresada == numeroReserva:
                print(f"Nombre Huesped: {nombreHuesped},\nDireccion: {direccion},\nCorreo: {correo},\nEdad: {edad}")
                if numeroAcompanantes > 3:
                    print(f"Numero Acompañantes: {numeroAcompanantes} (Huesped con demasiados acompañantes)")
                else:
                    print(f"Numero Acompañantes:{numeroAcompanantes} (Huesped dentro del limite de acompañantes)")
            else:
                print("Número de reserva no existe")

            next = input("presione enter para continuar\n")
        elif opcion == 3:
            print("*****Crear Admin*****")
            time.sleep(1)

            admin = input("Ingrese nuevo nombre de usuario\n")
            while admin == "":
                admin = input("Ingrese nuevo nombre de usuario valido\n")

            passAdm = input("Ingrese nueva contreaseña\n")
            while passAdm == "":
                passAdm = input("Ingrese nueva contreaseña valida\n")

            if admin != "" and passAdm != "":
                print("******Usuario admin creado con exito******")

            next = input("Presione enter para continuar\n")
        elif opcion == 4:
            print("*****Salir*****")
            print("Gracias por preferir Hotel 'Paradise Dreams'")
            break
        else:
            print("Opcion no valida")
    except:
        print("opcion no valida")
