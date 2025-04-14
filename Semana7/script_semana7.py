# Un módulo es un archivo en Python que agrupa funciones 
# y otros elementos reutilizables para organizar mejor el código.

# Una función es un bloque de código que realiza una tarea específica. 
# Puede recibir entradas (argumentos), ejecutar instrucciones y devolver 
# un resultado (salida).

# Para llamar a las funciones de un módulo, este debe estar en la misma 
# carpeta.

"""
Por ejemplo, para ejecutar este script, la estructura debe ser la siguiente
- carpeta:
    - script_semana7.py
    - conversion.py
    - operaciones.py
    - etc
"""




"""
Crea una función llamada area_circulo que reciba el radio 
de un círculo como parámetro y devuelva su área. Luego, pide 
al usuario que ingrese un radio y muestra el resultado usando la 
función."""
import math

def area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * radio ** 2

# Uso de la función
radio = float(input("Ingresa el radio del círculo: "))
print(f"El área del círculo es: {area_circulo(radio):.2f}")



"""
Crea un módulo llamado operaciones.py que contenga funciones para 
sumar, restar, multiplicar y dividir dos números. Luego, 
crea otro script que importe este módulo y use sus funciones.
"""


import operaciones

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
# operaciones.variable_global
print(f"Suma: {operaciones.sumar(a, b)}")
print(f"Resta: {operaciones.restar(a, b)}")
print(f"Multiplicación: {operaciones.multiplicar(a, b)}")
print(f"División: {operaciones.dividir(a, b)}")

"""
Crea un módulo llamado conversion.py con dos funciones: 
celsius_a_fahrenheit(celsius) y fahrenheit_a_celsius(fahrenheit). 
Luego, en otro script, importa este módulo y permite al usuario 
convertir temperaturas.
"""
import conversion

opcion = input("¿Convertir de Celsius a Fahrenheit (C) o de Fahrenheit a Celsius (F)? ").strip().upper()

if opcion == 'C':
    temp = float(input("Ingrese la temperatura en Celsius: "))
    print(f"Equivalente en Fahrenheit: {conversion.celsius_a_fahrenheit(temp):.2f}")
elif opcion == 'F':
    temp = float(input("Ingrese la temperatura en Fahrenheit: "))
    print(f"Equivalente en Celsius: {conversion.fahrenheit_a_celsius(temp):.2f}")
else:
    print("Opción no válida.")



"""
Crea un módulo llamado factorial.py que contenga una función recursiva 
para calcular el factorial de un número. Luego, usa este módulo en otro script.
"""
num = int(input("Ingrese un número para calcular su factorial: "))

if num < 0:
    print("El factorial no está definido para números negativos.")
else:
    print(f"El factorial de {num} es {operaciones.factorial(num)}")



"""
Crea un módulo primos.py con una función es_primo(n) que determine si un número 
es primo y otra función generar_primos(limite) que genere todos los números primos 
hasta un cierto límite. Luego, crea un script que importe este módulo y lo utilice.
"""

limite = int(input("Ingrese el límite para generar números primos: "))
print(f"Números primos hasta {limite}: {operaciones.generar_primos(limite)}")