# función que calcule el total de una factura. La función debe recibir la cantidad sin IVA,
# y devolver el total de la factura (recordemos que en Chile el IVA tiene el valor del 19%).
import math

# def precioIVA(valor):
#     # print("valor bruto", valor)
#     iva = 19 / 100
#     valorImpuesto = valor * iva
#     # print("valor neto", valorImpuesto)
#     valorNeto = valor + valorImpuesto
#     return int(valorNeto)
# valorBruto = int(input("Ingrese valor bruto (Sin impuestos)\n"))
# print(precioIVA(valorBruto))

# función que calcule el área de un círculo
# def areaCirculo():
#     radio = float(input("Escribe el radio: \n"))
#     # Calculando el área
#     area = math.pi * radio**2
#     print(f"El área del círculo es: {area:.2f}")
# areaCirculo()

# función que reciba una muestra de números en una lista y devuelva su media.


# listaNum = []
# listCuadrada = []
# while True:

#     def mediaNums(num):
#         listaNum.append(num)
#         media = sum(listaNum) / len(listaNum)
#         if len(listaNum) > 2:
#             print(listaNum)
#             return "la media es ", int(media)
#         else:
#             return "Sigue ingresando numeros"

#     valor = int(input("Ingresa numero\n"))
#     print(mediaNums(valor))


# función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
# def handleArrays(num):
#     listaNum.append(num)
#     cuadrado = num**2
#     listCuadrada.append(cuadrado)
#     print("listCuadrada", listCuadrada)
#     print("listaNum", listaNum)


# numero = int(input("Ingrense numero \n"))
# handleArrays(numero)

# función que reciba una cadena de caracteres y devuelva la cantidad de palabras


def cantidadPalabras(txt):
    listaPalabras = txt.split()
    return len(listaPalabras)

print("el texto contiene ", cantidadPalabras(input("escribe\n")), " palabras")


# función que reciba una cadena de caracteres y devuelva la cantidad de letras que contiene la frase
# def cantidadLetras(palabra):
#     print(len(palabra))


# cantidadLetras(input("escribe\n"))
