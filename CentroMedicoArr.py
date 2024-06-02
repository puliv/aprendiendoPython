import os, time

menuAbierto = True
subMenuAbierto = True
rutIncorrecto = True
rutConsultaIncorrecto = True
fechaIncorrecta = True
rutIncorrectoAtencion = True
edadIncorrecta = True
pacientes = []

while menuAbierto:
    os.system("cls")
    print("**********Centro Médico DUOC**********")
    print("1) Registrar Paciente")
    print("2) Atención Paciente")
    print("3) Gestionar Paciente")
    print("4) Salir")
    try:
        opcion = int(input("Ingrese opcion:\n"))
        if opcion == 1:
            crearPaciente = True
            while crearPaciente:
                print("**********Registrar Paciente**********")

                nombre = input("Ingrese nombre:\n")
                while nombre == "" or nombre == " ":
                    nombre = input("Ingrese nombre valido:\n")

                while rutIncorrecto:
                    # Validacion de numero entero que se debe hacer en prueba
                    rutString = input("Ingrese rut (sin guion ni puntos):\n")
                    while rutString == "" or rutString == " ":
                        rutString = input("Ingrese rut valido:\n")
                    try:
                        rut = int(rutString)
                        if rut < 5000000 or rut > 99999999:
                            print("Rut invalido")
                        else:
                            rutIncorrecto = False
                    except:
                        print("Rut solo acepta numeros")

                direccion = input("Ingrese direccion\n")

                while direccion == "" or direccion == " ":
                    direccion = input("Ingrese direccion valida:\n")

                correo = input("Ingrese correo:\n")
                while "@" not in correo:
                    correo = input("Ingrese correo valido:\n")

                while edadIncorrecta:
                    try:
                        edad = int(input("Ingrese edad paciente:\n"))
                        if edad < 0 or edad > 110:
                            print("Edad invalida")
                        else:
                            edadIncorrecta = False
                    except:
                        print("Edad solo acepta numeros")

                genero = input(
                    "Ingrese f o m para género del paciente segun corresponda:\n"
                ).lower()
                while genero != "f" and genero != "m":
                    print(f"------------{genero}-----------------")
                    genero = input("Ingrese genero de paciente valido:\n").lower()

                prevision = input(
                    "Ingrese prevision de salud: Fonasa(f) o Isapre(i)\n"
                ).lower()
                while prevision != "f" and prevision != "i":
                    prevision = input(
                        "Ingrese prevision de salud, solo acepta 'fonasa' o 'isapre'\n"
                    ).lower()

                paciente = [rut, nombre, direccion, correo, edad, genero, prevision]
                pacientes.append(paciente)
                time.sleep(1)
                # print(f"paciente, {paciente}")
                # print(f"arr pacientes, {pacientes}")

                agregarPaciente = input(
                    "Quieres agregar otro paciente?  's' o 'n'\n"
                ).lower()
                if agregarPaciente == "s":
                    rutIncorrecto = True
                    edadIncorrecta: True
                    continue
                else:
                    crearPaciente = False
        elif opcion == 2:
            rutIncorrectoAtencion = True
            print("**********Atención Paciente**********")
            while rutIncorrectoAtencion:
                rutPacienteStr = input("Ingrese rut (sin guion ni puntos):\n")
                print("rutPacienteStr", rutPacienteStr)
                while rutPacienteStr == "" or rutPacienteStr == " ":
                    rutPacienteStr = input("Ingrese rut valido:\n")
                try:
                    rutPaciente = int(rutPacienteStr)
                    print("rutPaciente", rutPaciente)
                    if rutPaciente < 5000000 or rutPaciente > 99999999:
                        print("Rut invalido")
                    else:
                        print("else ")
                        for pacienteSolicitado in pacientes:
                            if pacienteSolicitado[0] == rutPaciente:
                                print(pacienteSolicitado)
                                observaciones = input("Ingrese observaciones:\n")
                                if observaciones == "" or observaciones == " ":
                                    observaciones = input(
                                        "Ingrese observaciones validas:\n"
                                    )
                                else:
                                    pacienteSolicitado.append(observaciones)
                                    rutIncorrectoAtencion = False
                    print(pacienteSolicitado)
                    input("enter para continuar")
                except:
                    print("Rut solo acepta numeros")
        elif opcion == 3:
            subMenuAbierto = True
            os.system("cls")
            while subMenuAbierto:
                print("**********Gestionar Paciente**********")
                print("1) Consultar datos Paciente")
                print("2) Eliminar Paciente")
                print("3) Modificar Paciente")
                print("4) Regresar al menú principal")
                try:
                    subOpcion = int(input("Ingrese opcion:\n"))
                    if subOpcion == 1:
                        print("****Consultar datos Paciente****")
                        while rutConsultaIncorrecto:
                            rutConsultaStr = input(
                                "Ingrese rut para buscar paciente:\n"
                            )
                            while rutConsultaStr == "" and rutConsultaStr == " ":
                                rutConsultaStr = input("Ingrese rut valido:\n")
                            try:
                                rutConsulta = int(rutConsultaStr)
                                if rutConsulta < 5000000 or rutConsulta > 99999999:
                                    print("Rut invalido")
                                else:
                                    for pacienteConsultado in pacientes:
                                        if pacienteConsultado[0] == rutConsulta:
                                            print(f"Rut: {pacienteConsultado[0]}")
                                            print(f"Nombre: {pacienteConsultado[1]}")
                                            print(f"Direccion: {pacienteConsultado[2]}")
                                            print(f"Correo: {pacienteConsultado[3]}")
                                            print(f"Edad: {pacienteConsultado[4]}")
                                            print(f"Genero: {pacienteConsultado[5]}")
                                            print(
                                                f"Prevision Salud: {pacienteConsultado[6]}"
                                            )
                                            if pacienteConsultado[7]:
                                                print(
                                                    f"Observaciones: {pacienteConsultado[7]}"
                                                )
                                            input("Presione enter para continuar")
                                            rutConsultaIncorrecto = False
                            except:
                                print("Rut solo acepta numeros")
                        continue
                    elif subOpcion == 2:
                        rutConsultaIncorrecto = True
                        print("****Eliminar Paciente****")
                        while rutConsultaIncorrecto:
                            rutConsultaStr = input(
                                "Ingrese rut para eliminar paciente:\n"
                            )
                            while rutConsultaStr == "" and rutConsultaStr == " ":
                                rutConsultaStr = input("Ingrese rut valido:\n")
                            try:
                                rutConsulta = int(rutConsultaStr)
                                if rutConsulta < 5000000 or rutConsulta > 99999999:
                                    print("Rut invalido")
                                else:
                                    for pacienteConsultado in pacientes:
                                        if pacienteConsultado[0] == rutConsulta:
                                            try:
                                                pacientes.remove(pacienteConsultado)
                                                time.sleep(1)
                                                # print(pacientes)
                                                input("****Paciente eliminado****")
                                                input("Presione enter para continuar")
                                                rutConsultaIncorrecto = False
                                            except:
                                                print(
                                                    "Paciente no se encuentra en los registros"
                                                )
                            except:
                                print("Rut solo acepta numeros")
                        continue
                    elif subOpcion == 3:
                        print("****Modificar Paciente****")
                    elif subOpcion == 4:
                        print("****Regresando al menú principal****")
                        time.sleep(1.5)
                        subMenuAbierto = False
                    else:
                        print("Opcion no existe")
                except:
                    print("Opcion invalida")
        elif opcion == 4:
            print("**********Salir**********")
        else:
            print("opcion no existe")
    except:
        print("Ingrese solo numeros")
