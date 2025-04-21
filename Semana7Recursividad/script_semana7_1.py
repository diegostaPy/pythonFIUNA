"""
Crea un módulo llamado contador.py con una función 
contar_digitos(n) que reciba un número entero y 
retorne la cantidad de dígitos que tiene. 
Usa un bucle while en la implementación.
"""






def contar_digitos(n): ### colocar en un archivo contador.py al igual que las demas funciones de los siguientes ejercicios
    """Cuenta cuántos dígitos tiene un número entero."""
    if n == 0:
        return 1
    contador = 0
    while n != 0:
        n //= 10  # Dividir entre 10 para eliminar el último dígito
        contador += 1
    return contador


# import contador

num = int(input("Ingrese un número entero: "))
print(f"El número {num} tiene {contar_digitos(num)} dígitos.")

num = int(input("Ingrese un número entero: "))
print(f"El número {num} tiene {contar_digitos(num)} dígitos.")

"""
Crea un módulo llamado sumatoria.py con una función suma_rango(inicio, fin) 
que reciba dos números y retorne la suma de todos los números en ese rango 
usando un for.
"""
def suma_rango(inicio, fin):
    """Suma los números en el rango [inicio, fin]."""
    suma = 0
    for i in range(inicio, fin + 1):
        suma += i
    return suma


import sumatoria

inicio = int(input("Ingrese el número de inicio: "))
fin = int(input("Ingrese el número de fin: "))

print(f"La suma de los números entre {inicio} y {fin} es: {sumatoria.suma_rango(inicio, fin)}")


"""
Crea un módulo llamado palindromo.py con una función es_palindromo(cadena) 
que determine si una palabra o frase es un palíndromo (se lee igual de izquierda a 
derecha y viceversa). Usa un while.
"""
def es_palindromo(cadena):
    """Verifica si una palabra o frase es un palíndromo."""
    cadena = cadena.replace(" ", "").lower()  # Eliminar espacios y convertir a minúsculas
    izquierda, derecha = 0, len(cadena) - 1
    
    while izquierda < derecha:
        if cadena[izquierda] != cadena[derecha]:
            return False
        izquierda += 1
        derecha -= 1
    
    return True


import palindromo

texto = input("Ingrese una palabra o frase: ")

if palindromo.es_palindromo(texto):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")



"""
Crea un módulo fibonacci.py con una función generar_fibonacci(n) 
que genere los primeros n términos de la serie de Fibonacci usando 
un for.
"""
def generar_fibonacci(n):
    """Genera los primeros n números de la serie de Fibonacci."""
    if n <= 0:
        return []
    
    fibonacci = [0, 1] if n > 1 else [0]
    
    for _ in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    return fibonacci

import fibonacci

n = int(input("Ingrese la cantidad de términos de Fibonacci: "))

print(f"Serie de Fibonacci con {n} términos: {fibonacci.generar_fibonacci(n)}")



"""
Crea un módulo tablas.py con una función tabla_multiplicar(numero, hasta) que 
reciba un número y un límite, y muestre su tabla de multiplicar hasta ese límite 
usando un for.
"""
def tabla_multiplicar(numero, hasta):
    """Genera la tabla de multiplicar de un número hasta un límite."""
    tabla = []
    for i in range(1, hasta + 1):
        tabla.append(f"{numero} x {i} = {numero * i}")
    return tabla

import tablas

num = int(input("Ingrese un número para la tabla de multiplicar: "))
limite = int(input("Ingrese hasta qué número multiplicar: "))

print("\n".join(tablas.tabla_multiplicar(num, limite)))
