# Ejercicio 1: Crear una clase "Persona"

# Crea una clase llamada "Persona" con atributos como nombre, edad y género.
# Define un método llamado "presentarse" que imprima un mensaje que diga algo como "Hola, mi nombre es [nombre] y tengo [edad] años."
# Crea varias instancias de la clase "Persona" y llama al método "presentarse" en cada una

# class Persona:
#     def __init__(self, nombre, edad, genero):
#         self.nombre = nombre
#         self.edad = edad
#         self.genero = genero
        
#     def presentarse(self):
#         print(f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años')
        
# persona1 = Persona("Jorge", 15, "hombre")
# persona2 = Persona("Ricardo", 22, "hombre")
# persona3 = Persona("Mary", 35, "mujer")

# persona3.presentarse()


# Ejercicio 2: Crear una clase "Rectángulo"

# Crea una clase llamada "Rectángulo" con atributos longitud y ancho.
# Define métodos para calcular el área y el perímetro del rectángulo.
# Crea instancias de la clase "Rectángulo" con diferentes dimensiones y calcula su área y perímetro.


class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho
        
    def perimetro(self):
        return (self.longitud + self.ancho) * 2
    
    def area(self):
        return self.longitud * self.ancho
    
# rect1 = Rectangulo(10, 15)
# rect2 = Rectangulo(20,10)
# rect3 = Rectangulo(25,10)

# perimetro1 = rect1.perimetro()

# area1 = rect2.area()

# print(perimetro1)
# print(area1)


# Ejercicio 3: Crear una clase "Cuenta Bancaria"

# Crea una clase llamada "CuentaBancaria" con atributos como número de cuenta y saldo.
# Define métodos para depositar y retirar dinero de la cuenta.
# Asegúrate de que el saldo nunca sea negativo.
# Crea una instancia de la clase "CuentaBancaria" y realiza algunas transacciones.

class CuentaBancaria:
    def __init__(self, num_cuenta, saldo):
        self.num_cuenta = num_cuenta
        self.saldo = saldo
        
    def depositar(self, deposito):
        self.saldo += deposito
        return deposito
    
    def retirar(self, retiro):
        if self.saldo >= retiro and retiro > 0:
            return retiro
        else:
            return 'Saldo insuficiente'

cuenta1 = CuentaBancaria(6666, 500)
cuenta2 = CuentaBancaria(455, 100)

depo= cuenta1.depositar(1500)
extraccion = cuenta2.retirar(50)

print(f'Ud. ha depositado {depo} y el saldo de su cuenta es {cuenta1.saldo}')
print(extraccion)