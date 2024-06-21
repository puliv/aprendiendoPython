from functions import *

while True:
    mostrarMenu()
    try:
        option = int(input("Ingrese opcion\n"))
        if option == 1:
            limpiarTerminal()
            print("***Registrar Estudiante***")
            registrarEstudiante()
        elif option == 2:
            print("***Buscar Estudiante***")
            buscarEstudiante()
        elif option == 3:
            print("***Imprimir Certificados***")
        elif option == 4:
            print("***Eliminar Estudiante***")
        elif option == 5:
            print("***Salir***")
        else:
            print("opcion inválida")
    except:
        print("Opcion invalida except")
