import math, time, os

os.system("cls")

# función que calcule el total de una factura. La función debe recibir la cantidad sin IVA,
# y devolver el total de la factura (recordemos que en Chile el IVA tiene el valor del 19%).

print("******funcion impuestos******")


def precioIVA(valor):
    iva = 19 / 100
    valorImpuesto = valor * iva
    valorNeto = valor + valorImpuesto
    return print("Valor ingresado + impuestos (19%): ", int(valorNeto))


valorBruto = int(input("Ingrese valor bruto (Sin impuestos)\n"))
precioIVA(valorBruto)


time.sleep(1)
# función que calcule el área de un círculo
print("******funcion area circulo******")


def areaCirculo():
    radio = float(input("Ingresa el radio de un circulo: \n"))
    # Calculando el área
    area = math.pi * radio**2
    return print(f"El área del círculo es: {area:.2f}")


areaCirculo()

time.sleep(1)
# función que reciba una cadena de caracteres y devuelva la cantidad de palabras
print("******funcion que devuelve la cantidad de palabras******")


def cantidadPalabras(txt):
    listaPalabras = txt.split()
    print("el texto contiene ", len(listaPalabras), " palabras")


cantidadPalabras(input("ingresa un texto:\n"))


time.sleep(1)
# función que reciba una cadena de caracteres y devuelva la cantidad de letras que contiene la frase
print("******funcion que devuelve la cantidad de letras******")


def cantidadLetras(palabra):
    print("El texto tiene ", len(palabra), " letras")


cantidadLetras(input("ingresa un texto:\n"))

listaNum = []
numList = []
listCuadrada = []
funcionMediaAbierto = True
funcionCuadradoAbierto = True
time.sleep(1)
print("******funcion que devuelve la media de la lista******")
while funcionMediaAbierto:
    # función que reciba una muestra de números en una lista y devuelva su media.

    def mediaNums(num):
        listaNum.append(num)
        media = sum(listaNum) / len(listaNum)
        if len(listaNum) > 2:
            print(listaNum)
            return "la media es ", int(media)
        else:
            return "Sigue ingresando numeros"

    if len(listaNum) > 2:
        seguir = int(input("Quieres continuar? 1) Si 2) No:\n"))
        if seguir == 1:
            valor = int(input("Ingresa numero\n"))
        else:
            funcionMediaAbierto = False
    else:
        valor = int(input("Ingresa numero\n"))
    print(mediaNums(valor))

time.sleep(1)
# función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
print("******funcion que devuelve lista con numeros ingresados al cuadrado******")
while funcionCuadradoAbierto:

    def handleArrays(num):
        numList.append(num)
        cuadrado = num**2
        listCuadrada.append(cuadrado)
        print("listCuadrada", listCuadrada)
        print("numList", numList)

    if len(numList) > 2:
        seguir = int(input("Quieres continuar? 1) Si 2) No:\n"))
        if seguir == 1:
            numero = int(input("Ingresa numero\n"))
        else:
            funcionCuadradoAbierto = False
    else:
        numero = int(input("Ingresa numero\n"))
    handleArrays(numero)


print("************FIN************")
