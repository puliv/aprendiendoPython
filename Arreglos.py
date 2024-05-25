import os, time

os.system("cls")


# Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en
# una lista, luego el sistema deberá mostrar el nombre que tenga mayor cantidad de
# caracteres en un mensaje de salida por pantalla
# names = []
# large = 0  # variable para iniciar comparacion entre nomnbres
# for x in range(3):
#     name = input(f"Ingrese nombre {x+1} \n")
#     names.append(name)  # Agregando nuevo nombre al arreglo
# # Comparando largos de nombres ingresados
# for i in names:
#     if len(i) > large:
#         large = len(i)  # guardando largo de nombre
#         longestName = i  # nombre mas largo
# print(f"Nombre mas largo {longestName}")


# Cree 2 listas, en las cuales se guardará 3 nombres y 3 apellidos (1 lista para
# nombres y una 1 lista para apellidos), el sistema deberá mostrar de forma ordenada
# los nombres y apellidos
# names = []
# lastnames = []
# for x in range(3):
#     name = input(f"Ingrese nombre {x+1} \n")
#     lastname = input(f"Ingrese apellido {x+1} \n")
#     names.append(name)
#     lastnames.append(lastname)
# time.sleep(0.5)
# for i in range(3):
#     print(f"{names[i]} {lastnames[i]}")

# Cree una lista y comience a almacenar nombres, cada vez que se agregue un
# nombre nuevo, el sistema preguntará si desea agregar otro nombre, deberá agregar
# nombres hasta que la respuesta sea “no”, “No”, “nO” o “NO” (use funciones lower()
# y upper() ) .
# Una vez ingresa n nombres, deberán eliminar el nombre con la menor cantidad de
# caracteres

# nombres = []
# keepAddingNames = True
# while keepAddingNames:
#     nombre = input("Agrega un nombre \n")
#     nombres.append(nombre)
#     question = input("Deseas agregar otro nombre? \n").lower()
#     if question == "no":
#         print("Hasta nuncaaaaa")
#         keepAddingNames = False

# Cree un menú para registrar usuarios e iniciar sesión, también el menú tendrá la
# opción de eliminar usuarios, para ello, utilice el nombre de usuario, además para
# confirmar la eliminación, deberán escribir la contraseña correspondiente de cada
# usuario
# 1. Inicio sesión.
# 2. Registrar usuario
# 3. Eliminar usuario.
# 4. Salir.
# La opción 1 solo mostrará un mensaje exitoso si ha iniciado correctamente,
# o un error de caso contrario.

openMenu = True
users= []
passwords = []
while openMenu:
    print("1. Inicio sesión")
    print("2. Registrar usuario")
    print("3. Eliminar usuario.")
    print("4. Salir.")
    try:
        opcion = input("Ingrese opcion \n")
        if opcion == 1:
            print("***iniciar sesión***")
            user = input("Ingrese nombre de usuario: \n")
            password = input("Ingrese contraseña: \n") 
        elif opcion == 2:
            print("***Registrar usuario***")
        elif opcion == 3:
            print("***Eliminar usuario***")
        elif opcion == 4:
            print("***Salir***")
            openMenu = False
        else:
            print("opcion invalida")
    except:
        print("opcion invalida")
