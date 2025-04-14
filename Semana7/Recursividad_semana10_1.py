"""
FIBONACCI
"""
# def fibonacci(n): # Ineficiente para grandes valores de n
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(6))  

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

fibonacci_memo(6)

"""
suma de elementos de una lista
"""

def suma_lista(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

print(suma_lista([4, 3, 2, 1]))  

"""
Calcular de forma recursiva a^b (asumiendo que b >= 0).
"""

def expo(a, b):
    if b < 0:
        b = b * -1
    if b == 0:
        return 1
    else: 
        return a * expo(a, b - 1)

# a = 2
# while (1):
#     try: 
#         b = int(input())
#     except ValueError:
#         print("b no es un int")
#     except: 
#         print("error")
#     if b < 0:
#         print("b es negativo")
#     else:
#         break
# print(expo(2, -3))


"""
Contar cuántas veces aparece un número en una lista
"""
def contar_apariciones(lista, x):
    if lista == []:
        return 0
    elif lista[0] == x:
        return 1 + contar_apariciones(lista[1:], x)
    else:
        return contar_apariciones(lista[1:], x)

print(contar_apariciones([1, 2, 3, 2, 4, 2], 5))

"""
Potencia de un número
"""
def potencia(a, b):
    if b == 0:
        return 1
    else:
        return a * potencia(a, b - 1)

print(potencia(2, 4)) 

"""
Verificar si una cadena es palíndroma
"""
def es_palindromo(cadena):
    if len(cadena) <= 1:
        return True
    elif cadena[0] != cadena[-1]:
        return False
    else:
        return es_palindromo(cadena[1:-1])

print(es_palindromo("reconocer"))
print(es_palindromo("python"))
