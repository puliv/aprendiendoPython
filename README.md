# aprendiendoPython
Repositorio para guardar los ejercicios desarrollados con Python en clases de programación

Hotel Paradise:
El Hotel "Paradise Dreams" desea implementar un sistema informático para la gestión
de sus huéspedes. A continuación, se detallan los requisitos para el desarrollo:
Se te solicita crear un menú en el cual se puedan registrar los datos de un huésped. Los
atributos que debe tener la ficha son los siguientes:
Número de Reserva
Nombre del huésped
Dirección
Correo electrónico
Edad
Número de acompañantes

El menú debe tener las siguientes opciones:

Sistema de Gestión de Huéspedes
1) Registrar Huésped
2) Consultar Datos de Huésped
3) Salir
Donde:
Registrar Huésped: Solicita todos los datos de un huésped para hacer el registro de una
nueva ficha. Cada uno de los atributos debe cumplir con lo solicitado mediante
validación.
- Nombre del huésped: no puede estar vacío.
- Dirección: no puede estar vacía.
- Número de Reserva: debe ser un número entero que se encuentre dentro del rango
de 1000 y 9999.
- Edad: debe ser un número entero que se encuentre en el rango de 18 a 120.
- Correo electrónico: debe ser una cadena de caracteres que contenga al menos un
carácter "@".
- Número de acompañantes: debe ser un número entero mayor o igual a cero.
Consultar Datos de Huésped:
Muestra por pantalla todos los atributos del huésped que coincidan con el número de
reserva ingresado. Los datos se deben mostrar de forma ordenada, utilizando
herramientas de tabulación y/o saltos de línea según lo aprendido en clases (ver reglas
de negocio más abajo).
Salir:
Sale del ciclo del menú y muestra un mensaje "Gracias por preferir Hotel 'Paradise
Dreams' ".
Reglas de negocio:
Debe crearse un usuario y una contraseña para el administrador. Solo este usuario
tiene permisos para visualizar la opción 2.
- Ejemplo:
- Usuario: seller
- Contraseña: 123
En el resumen (opción 2), deberá desplegarse toda la información del huésped y, si el
número de acompañantes es superior a 3, el sistema deberá indicar 'huésped con
demasiados acompañantes’; caso contrario, 'huésped dentro de límite de
acompañantes'.