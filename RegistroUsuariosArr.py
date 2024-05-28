# Agregar usuarios a arreglo de usuarios
# Eliminar usuarios del arreglo
# Buscar usuarios en el arreglo
import os, time

usuarios = []
registroIncompleto = True
os.system("cls")
while registroIncompleto:
    idDeleteIncorrecto = True
    try:
        print("Ingrese 1) para agregar usuarios ")
        print("Ingrese 2) para eliminar usuarios ")
        print("Ingrese 3) para salir ")
        opcion = int(input("Ingrese opcion\n"))

        if opcion == 1:
            # os.system("cls")
            print("*******Agregar usuarios*******")
            usersNum = int(input("Cuantos usuarios vas a agregar?\n"))
            for x in range(usersNum):
                idIncorrecto = True
                nivelIncorrecto = True
                try:
                    while idIncorrecto:
                        try:
                            id = int(input(f"Ingrese id de usuario {x+1}\n"))
                            if id != "":
                                idIncorrecto = False
                        except:
                            print("Solo se permiten numeros")
                    nombre = input(f"Ingrese nombre de usuario {x+1}\n")
                    while nombre == "":
                        nombre = input("Ingrese nombre válido\n")
                    correo = input(f"Ingrese correo de usuario {x+1}\n")
                    while "@" not in correo:
                        correo = input("Ingrese correo válido\n")
                    while nivelIncorrecto:
                        try:
                            nivel = int(
                                input(f"Ingrese nivel del usuario {x+1} (1 al 100)\n")
                            )
                            if nivel < 1 or nivel > 100:
                                nivel = int(input("Ingrese nivel válido\n"))
                            else:
                                nivelIncorrecto = False
                        except:
                            print("Solo se permiten numeros del 1 al 100")

                    usuario = {
                        "id": id,
                        "nombre": nombre,
                        "correo": correo,
                        "nivel": nivel,
                    }
                    usuarios.append(usuario)
                except:
                    print("Ingresa opciones validas")

            for y in usuarios:
                print(y)

            # Obteniendo el id mas bajo en el arreglo
            # idMinimo = min(usuario["id"] for usuario in usuarios)
            # print(f"Id mas chico? {idMinimo}")

        elif opcion == 2:
            # os.system("cls")
            print("*******Eliminar usuario*******")
            while idDeleteIncorrecto:
                try:
                    idDelete = int(input("Para eliminar un usuario ingrese Id\n"))
                    if idDelete != "":
                        for usuario in usuarios:
                            if usuario["id"] == idDelete:
                                usuarios.remove(usuario)
                                print(f"Usuario Id:{idDelete} eliminado")
                                for a in usuarios:
                                    print(f"lista de usuarios actualizada: {a}")
                                idDeleteIncorrecto = False
                            else:
                                print("id no se encuentra en esta lista")
                except:
                    print("Id solo acepta numeros")

        elif opcion == 3:
            print("salir")
            time.sleep(1)
            registroIncompleto = False
    except:
        print("Ingrese opcion valida")
