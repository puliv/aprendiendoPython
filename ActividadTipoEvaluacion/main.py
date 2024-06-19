from functions import *
import random

while True:
    showMenu()
    try:
        option = int(input("Ingrese opcion\n"))
        if option == 1:
            clearConsole()
            print("***Registrar Estudiante***")
            registarEstudiante()
        elif option == 2:
            print("2")
        elif option == 3:
            print("3")
        elif option == 4:
            print("4")
        else:
            print("opcion invalida")
    except:
        print("Opcion invalida")
