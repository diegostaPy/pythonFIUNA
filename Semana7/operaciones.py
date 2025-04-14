def sumar(a, b):
    return a + b

variable_global = 13

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

# def validar(a, n): # n=1-> int, n=2->flat
#     if n == 1:
#         intrucciones que validen este tipo de variable.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generar_primos(limite):
    return [n for n in range(2, limite + 1) if es_primo(n)]
