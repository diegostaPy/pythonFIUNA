def imprimir(L):
    for num in L:
        print(str(num)+" ",end="")
n=int(input())
L1=input()
L1v1=L1.split(" ")
#print(L1v1)
L1v2=[]
for caracter in L1v1:
    L1v2.append(int(caracter))
#print(L1v2)
#opcion1
#L1v3=set(L1v2)
#L1v4=list(L1v3)
#print(L1v4)
#opcion2
L2=[]
#L1unica=[]

for elemento in L1v2:
 #   if not(elemento in L1unica):
    if not(elemento in L2[::2]):
  
       # L1unica.append(elemento)
        L2.append(elemento)
        cantidad=L1v2.count(elemento)
        L2.append(cantidad)
#print(L2)
imprimir(L2)