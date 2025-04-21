#Determinar si un número es primo
p=int(input())
contador=0
for i in range(2,p):
    if(p%i==0):
        contador=contador+1
    
if(contador==0):
    print("El número es primo")
else:
    print("El número no es primo")