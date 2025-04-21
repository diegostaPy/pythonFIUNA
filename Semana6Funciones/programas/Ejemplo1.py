from Fibonacci import *

n = int(input("Ingrese el valor de N: "))
#print(fib(n))
#print(fib2(n))

print(x := fib2(n))
del x[0]

for i in x:
    print(f"{i} Es primo" if esPrimo(i) else f"{i} No es Primo")
    