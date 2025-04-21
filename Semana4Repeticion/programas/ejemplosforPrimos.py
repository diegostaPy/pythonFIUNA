x=int(input())
contador=0
for i in range(2,x):# range(desde, hasta, paso)
    if(x%i==0):
        contador=contador+1
if(contador==0):
    print("El número es primo")
else:
    print("El número no es primo")