# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
# Array

v = ["Hola", "Mundo", 4.3, True, ["otro", "Array", "Dentro"]]

v2 = ["Hola", "Mundo"]

v3 = [1, 2, 3, 4, 5, 6, 7, 8]

v4 = range(1, 200)

v5 = range(201)

for x in v5:
    print(x)

print(v5[200])

# Modificar elemento del vector
v[4] = "Orlando"

# Eliminar elemento

v.remove(4.3)

# Eliminar el último elemento

v.pop()
v.pop(0)

# Agregar elemento

v.append("E")
v.insert(1, "Orlando")

# Borrar todos los elementos

v.clear()

# Conocer la posición de un elemento

v2.index("Mundo")

# Número de elementos
len(v3)

# Número de veces que aparece un elemento dentro del vector
v3.count(5)

# Ordenar un vector

a = [5, 7, 4, 8, 9, 2, 3, 0]

a.sort()

# Conocer si un elemento está o no dentro del vector

4 in a
6 in a

"Hola" in v2

# Acceder a un elemento de un array interno

# Forma 1
aux = v[-1]
aux = aux[0]
print(aux)

# Forma 2
aux = v[-1][0]
print(aux)

# Matriz

m = [[2, 4], [4, 2]]

# Recorrer vector

for x in v3:
    print(v3)

vaux = v[2:5]

for x in vaux:
    print(vaux)

# Ejercicio

Tamaño = input

Tamaño = Tamaño + 1

vector = range(input + 1)

print(vector)









































