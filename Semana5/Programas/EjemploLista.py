'''
n = int(input("Ingrese n: "))
a = 0
b = 1

for i in range(n):
    print(a, end=", ")
    a,b = b,a+b
'''
#Se lee la cantidad de elementos
N = int(input("Ingrese la cantidad de elementos: "))
#Se leen los elementos de la lista
A = [] #Lista vacía de nombre A
for i in range(N):
    x = int(input(f"Ingrese A[{i}]: "))
    A.append(x) #Agregamos x al final de la lista
print("El tamaño de la lista es:", len(A))
#Impresión de la lista - Forma 1
print("\nLa lista es (1):")
print(A)
#Impresión de la lista - Forma 2
print("\nLa lista es (2):")
for i in range(N):
    print(f"A[{i}] = {A[i]}")
