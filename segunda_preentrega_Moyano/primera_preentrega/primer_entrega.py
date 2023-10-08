# Crear un programa que permita emular el registro y almacenamiento de usuarios en una base de datos. Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales.

# El formato de registro es: Nombre de usuario y Contraseña.
# Utilizar una función para almacenar la información y otra función para mostrar la información.
# Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).
# Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.

import json
import os
users = {}

def reg_user():
    user = input('Ingrese su nombre de usuario: ').upper()
    password = input('Ingrese una contraseña: ')
    users[user] = password
    print(f"El usuario {user} se ha registrado satisfactoriamente. Contraseña guardada")
    save_db()

def login():
    user = input('Ingrese su usuario: ').upper()
    if user in users:
        while True:
            password = input('Ingrese su contraseña: ')
            if users[user] == password:
                print('Ingreso de sesion exitoso')
                break
            else:
                print('Contraseña incorrecta. Vuelva a intentarlo')
    else:
        print('El usuario no está registrado')
        
def save_db():
    with open("midb.json", "w") as archivo:
        json.dump(users, archivo)

# Función para cargar la base de datos desde un archivo JSON
def open_db():
    if os.path.exists("midb.json"):
        with open("midb.json", "r") as archivo:
            users.update(json.load(archivo))


def read_db():
    if os.path.exists("midb.json"):
        with open("midb.json", "r") as archivo:
            db = json.load(archivo)
            for user in db.keys():
                print(f'Los usuarios registrados en la base de datos son: {user}')
            
open_db()
        
while True:
    print('''
          Bienvenido! Por favor, elija una opcion:
          - Seleccione 1 para iniciar la sesion
          - Elija 2 para crear un usuario
          - Opcion 3 para Salir
          ''')
    
    option = input('Elija una de las ocpiones del menu. ')
    
    if option == '1':
        login()
    elif option == '2':
        reg_user()
    elif option == '3':
        print('Gracias por usar nuestros servicios. Hasta la proxima')
        break
    else:
        print('Por favor, elija una opcion válida')
        
read_db()