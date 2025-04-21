N=10
lista=[]
print(type(lista))
for i in range(N):
    entrada=i+1
    lista.append(entrada)
 
print(lista)
lista2=[1, 2.3, 3, 4,4, 5, 6, 7, 8, 9, 10]

print(lista2[1])
print(lista2[-1])
print(lista2.index(4))
print(lista2.count(3))
print(lista2.count(11))
A=[10,21,2,-6]
print(A[1:3])
print(A[1:])
print(A[:])
B=A
C=A[:]
A[0]=11
print(A)
print(B)
print(C)
print(A+[12,1])
print(21 not in A)

print("A"+chr(65))

print(ord("A"))
nombre="juan"
for x in nombre:
    print(chr(ord(x)-32),end="")
print(nombre.upper())
cadena="1,2,3,4,5"
lista=cadena.split(",")
print(lista)

numero=input("Cargar un numero:")
while  not numero.isdigit():
    numero=input("el progrma solo acepta numeros")
print("carga correcta de datos")    
n=int(numero)   
print(n)