import math
# -*- coding: utf-8 -*-

# Comentario de línea

"""
Comentario
de
parrafo
"""
# Hola mundo
print("Hola mundo")

# Variables

x = 4  # Int
y = "Texto"  # String
z = 4.5  # Float
a = True  # Booleano
b = False  # Booleano
c = 4 + 5j  # Complejo
print(x, y, z, a, b, c)  # Imprime el valor de cada variable
print("x" + y + "z" + "a" + "b" + "c")  # Imprime cada variable como String
print(type(b))  # Imprime el tipo de dato de la variable

# Conversion de tipos de datos

# Enteros
x = int(2)
print(x)

x = int(2.8)
print(x)

x = int("2.8")
print(x)

# Float
x = float(2)
print(x)

x = float("2")
print(x)

x = float("2.8")
print(x)

cad = "Hola Mundo"
print(cad[0])
print(cad[2])
print(cad[0:5])  # No toma el último valor

cad = "    Hello World     "
cad = cad.strip()
print(cad)
print(cad[0])

cad = "Hello World"
print(len(cad))
print(cad.lower())
print(cad.upper())
print(cad.replace('1', 'y'))
print(cad.split(" "))
print(cad.split("1"))

# Operaciones aritmeticas

# Opraciones Aritméticas

a = 20
b = 3
c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a / b
print(c)
c = a // b
print(c)
c = a % b
print(c)
c = a ** b
print(c)
c = math.sqrt(a)
print(c)
c = math.pi
print(c)


# Captura por consola

print("Digite el nombre")
nombre = input()
print("Hola "+nombre+" !")

print("Digite número 1")
n1 = input()
print("Digite número 2")
n2 = input()
n1 = float(n1)
n2 = float(n2)
print(n1+n2)


















