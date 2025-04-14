"""
La recursividad es una técnica de programación en la que una 
función se llama a sí misma para resolver un problema. Se usa 
cuando un problema puede dividirse en subproblemas más pequeños 
del mismo tipo.

Una función recursiva debe tener dos partes esenciales:

Caso base (o condición de parada):
Es la condición que detiene la recursión. Sin esto, la función se 
llamaría infinitamente y causaría un error (desbordamiento de pila 
o stack overflow).

Llamada recursiva:
Es cuando la función se llama a sí misma, pero con un problema más 
simple que va acercándose al caso base.
"""
"""
### Ejemplo 1: Contar hacia atrás
def contar_hasta_cero(n):
    if n < 0:  # Caso base
        print("¡Listo!")
    else:
        print(n)
        contar_hasta_cero(n - 1)  # Llamada recursiva

contar_hasta_cero(3)

### Factorial de un nro
def factorial(n):
    if n == 0:
        return 1  # Caso base
    else:
        print(n)
        return n * factorial(n - 1)  # Llamada recursiva

print(factorial(6))

### Suma de los primeros N nros naturales
def suma_naturales(n):
    if n == 0:
        return 0  # Caso base
    else:
        return n + suma_naturales(n - 1)

print(suma_naturales(4))

### Contar elementos de una lista (sin usar len())
def contar_elementos(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + contar_elementos(lista[1:])

# Ejemplo
print(contar_elementos([1, 2, 3, 4, 5]))  # 4

### Invertir un String
def invertir_cadena(cadena):
    if cadena == "":
        return ""  # Caso base
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]

print(invertir_cadena("hola"))
"""

### Buscar un nro en una lista
def contiene(lista, objetivo):
    if lista == []:
        print(lista)
        return False
    elif lista[0] == objetivo:
        print(lista)
        return True
    else:
        print(lista)
        return contiene(lista[1:], objetivo)

# print(contiene([1, 3, 5, 7], 5))
print(contiene([1, 3, 5, 7], 2))
string = "-123"
if "-1" in string:
    print("...")
