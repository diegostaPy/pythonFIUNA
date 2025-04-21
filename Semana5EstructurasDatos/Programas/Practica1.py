import math
n = 0
while n!=int(n) or n<=0:
	n = float(input("Ingrese un numero entero y positivo: "))
n = int(n)
fact = 1
for i in range(1, n): #[2,3,4,5...n]
    fact *= i  #fact = fact * i

print(f"El factorial de {n} es : {fact} ")
print(f"The factorial de {n} es : {math.factorial(n)} ")
