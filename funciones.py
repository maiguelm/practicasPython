# Ej. 2

# numeros = [2,6,8,9,3,12,56,47,25]

# def media(numeros):
#     return sum(numeros) / len(numeros)
    
    
# print(f"la media de la suma de los numeros de la lista {numeros} es {media(numeros)}")

# Ej. 3

# def es_multiplo(num1, num2):
# 	if num1 % num2 == 0:
# 		return True
# 	else:
# 		return False

# num1 = int(input("Ingrese el primer valor: "))
# num2 = int(input("Ingrese el segundo valor: "))

# if es_multiplo(num1,num2):
#     print(f"El {num1} es multiplo de {num2}")
# else:
# 	print(f"Los numeros {num1} y {num2} no son muiltiplos")

#Ejercicio años bisiestos


# def anio_bisiesto(anio):
#     if not isinstance(anio, int):
#        return "Ingrese un numero válido"
#     elif (anio % 4 == 0 & anio % 400 != 0) or (anio % 400 == 0):
#         return "El año es bisiesto"
#     else:
#         return "El año no es bisiesto"

# anio = int(input("Ingrese un año: "))
# resultado = anio_bisiesto(anio)
# print(resultado)
# print(hex(id(resultado)))


# Ejercicio 1

# Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura

import math


# base = int(input("Ingrese la base: "))
# altura = int(input("Ingrese la altura: "))

# def area_rectangulo(base, altura):
#     return base * altura

# print(area_rectangulo(base,altura))

#Ejercicio 2
# Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio

# def area_circulo(radio):
#     area = round((math.pi * radio **2), 2)
#     return area

# radio = float(input("Ingrese el radio del circulo en centímetros: "))

# print(f"El area del circulo es {area_circulo(radio)} centímetros")


# Ejercicio 3
# Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

# Si el primer número es mayor que el segundo, debe devolver 1.
# Si el primer número es menor que el segundo, debe devolver -1.
# Si ambos números son iguales, debe devolver un 0

# def relacion(num1, num2):
#     if num1 > num2:
#         return 1
#     elif num1 < num2:
#         return -1
#     else:
#         return 0
    
# num1 = input("Ingrese el primer numero: ")
# num2 = input("Ingrese el segundo numero: ")

# print(f'la relacion de los numeros ingresados es {relacion(num1,num2)}')

# Ejercicio 4
# Realiza una función llamada intermedio() que, a partir de dos números, devuelva su punto intermedio:

# def intermedio(num1, num2):
#     return (num1 + num2) /2

# num1 = int(input("Ingrese el primer numero: "))
# num2 = int(input("Ingrese el segundo numero: "))

# print(f'El punto intermedio entre {num1} y {num2} es {intermedio(num1, num2)}')

#Ejercicio 4 bis
# Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:

# def separar(lista):
#     pares = []
#     impares = []
    
#     for numero in lista:
#         if numero % 2 == 0:
#             pares.append(numero)
#         else:
#             impares.append(numero)
            
#     pares.sort()
#     impares.sort()
    
#     return pares, impares

# lista = [5,12,4,6,58,75,69,63,25]

# pares, impares = separar(lista)

# print(f'La lista de numeros pares es {pares}')
# print(f'La lista de numeros impares es {impares}')

#EJERCICIO 5
# Realiza una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

# Devolver el límite inferior si el número es menor que éste
# Devolver el límite superior si el número es mayor que éste.
# Devolver el número sin cambios si no se supera ningún límite.
# Comprueba el resultado de recortar 15 entre los límites 0 y 10

# def recortar(num, inferior, superior):
#     if num > superior:
#         return superior
#     elif num < inferior:
#         return inferior
#     else:
#         return num
    
# print(recortar(5,0,10))


# Ejercicio: Calculadora Simple

# Crea una calculadora simple que realice operaciones de suma, resta, multiplicación y división. Debes hacerlo mediante el uso de funciones separadas para cada operación.

# Instrucciones:

# Crea una función llamada suma que tome dos números como argumentos y devuelva la suma de los mismos.

# Crea una función llamada resta que tome dos números como argumentos y devuelva la resta del primero menos el segundo.

# Crea una función llamada multiplicacion que tome dos números como argumentos y devuelva el producto de los mismos.

# Crea una función llamada division que tome dos números como argumentos y devuelva el resultado de la división del primero entre el segundo. Asegúrate de manejar el caso de división por cero.

# En el programa principal, permite al usuario seleccionar una operación (suma, resta, multiplicación o división) y luego ingresar dos números. Luego, utiliza la función correspondiente para realizar la operación seleccionada e imprime el resultado.

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

def calculadora():
    operacion = input('''Ingrese la operacion a realizar:
            - Escriba 1 para Sumar
            - Escriba 2 para restar
            - Escriba 3 para multiplicar
            - Escriba 4 para dividir
             ''')
    
    num1 = float(input('Ingrese el primer número: '))
    num2 = float(input('Ingrese el segundo numero: '))
    
    
    if operacion == "1":
        resultado = suma(num1, num2)
    elif operacion == "2":
        resultado = resta(num1, num2)
    elif operacion == "3":
        resultado = multiplicar(num1, num2)
    elif operacion == "4":
        resultado = dividir(num1, num2)
    else:
        print("Ingrese una opcion válida")
    
    print(f"El resultado de la operacion con {num1} y {num2} es igual al {resultado}")
    
calculadora()