n = 0
while n!=int(n) or n<=100:
	n = float(input("Ingrese un numero entero y positivo: "))
suma = 0
cont = 0
prod = 1
n = int(n)
multiplos = []
for i in range(1,n+1,2):
    if(i%5!=0): 
        multiplos.append(i)
        cont += 1
        suma += i
        prod *= i

print(multiplos)
print(f"La cantidad es: {cont}")
print(f"La cantidad len es: {len(multiplos)}")
print(f"La suma con sum es: {sum(multiplos)}")
print(f"La suma es: {suma}")
print(f"El promedio es: {suma/cont}")
print(f"El producto es: {prod}")


