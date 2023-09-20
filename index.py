""" jugados = 20

puntos_ganados = 3
puntos_empatados = 1
puntos_perdidos = 0

partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))
partidos_empatados = int(input("Ingrese la cantidad de partidos empatados: "))
partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos:"))


puntos_totales = (partidos_ganados * puntos_ganados + partidos_empatados)
promedio = puntos_totales / jugados

print("El promedio de puntos obtenidos fue: ", promedio)
print(f"Los puntos obtenidos fueron {puntos_totales}") """

#DESAFIO STRINGS
""" cadena_1 = "versatil"
cadena_2 = "Python"
cadena_3 = "es un lenguaje"
cadena_4 = "de programacion"

final = f"{cadena_2} {cadena_3} {cadena_4} {cadena_1}"

print(final) """

#DESAFIO CADENAS
""" cadena = "acitametaM ,5.8 ,otipeP ordeP"

cadena_volteada = cadena[::-1]

nombre_alumno = cadena_volteada[0:12]
nota = cadena_volteada[14:17]
materia = cadena_volteada[19:]
cadena_formateada = f"{nombre_alumno} ha sacado una nota de {nota} en {materia}"

print(materia)
print(cadena_formateada)
 """
 
#EJERCICIO SETS CLASE 6
""" colores = {"rojo", "blanco","azul"}

colores.update(["violeta", "dorado"])
print(colores)

colores.discard("celeste")
colores.discard("blanco")
colores.discard("dorado")

print(colores) """

"""# Ej 2 Sets (10min)
Programa las siguientes instrucciones de forma ordenada sobre la variable grupo:
1. Añade los usuarios: Ana, Ramón, Marta, Eric, David
2. Elimina los usuarios: Mario, Miguel, Esteban
"""
""" 
grupo = {'Miguel', 'Blanca', 'Mario', 'Andrés'}
grupo.update(["Ana", "Ramón", "Marta", "Eric", "David"])
print(grupo)

grupo.discard("Esteban")
grupo.remove("Mario")
grupo.remove("Miguel")
print(grupo)
print(type(grupo)) """


#serie fibonacci

""" def fibonacci_hasta_n(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b

# Ejemplo de uso:
numero_dado = 1150  # Cambia este valor al número hasta el cual deseas mostrar la serie
fibonacci_hasta_n(numero_dado)
 """
 
""" numero_veces = int(input("Ingrese un numero: "))
nombre = input("ingrese su nombre: ")
print((nombre + "\n") * numero_veces) """

# nombre = input("Ingrese su nombre completo: ")

# print(nombre.lower() + "\n", nombre.upper() + "\n", nombre.title())

# print(f"Su nombre es {nombre.upper()} y tiene {len(nombre)} letras")


# frase = input("Ingrese una frase: ")
# print(frase[::-1])

# vocal = input("ingrese una vocal: ")
# print(frase.replace(vocal, vocal.upper()))

#Ejercicio 3

# numero_uno = int(input("Ingrese un numero: "))
# numero_dos = int(input("Ingrese el segundo numero: "))

# while True:
#     opcion = input("""
#           Seleccione una de las siguientes opciones:
#           1.- Sumar los dos números;
#           2.- Restar los dos números (el primero menos el segundo);
#           3.- Multiplicar los números;
#           4.- Salir 
#           """)
    
#     if opcion == "1":
#         print(f"el resultado de la suma de {numero_uno} mas {numero_dos} es {numero_uno + numero_dos}")
#     elif opcion == "2":
#         print(f"el resultado de la resta de {numero_uno} menos {numero_dos} es {numero_uno - numero_dos}")
#     elif opcion == "3":
#         print(f"el resultado de la multiplicacion de {numero_uno} por {numero_dos} es {numero_uno * numero_dos}")
#         break
#     elif opcion == "4":
#         break
#     else:
#         print("Elija una opcion correcta")
        
#Ejercicio 3-2

# while True:
#     numero = int(input("Introduzca un numero par: "))
#     if numero%2 == 0:
#         print(f"El número ingresado es {numero} y es par")
#         break
#     print("Vuelva a ingresar un numero")
        

# Ejercicio 3-3
