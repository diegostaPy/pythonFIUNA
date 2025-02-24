"""Desarrolle un algoritmo que permita realizar 
la división entre dos números enteros mediante 
restas sucesivas."""
dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))
cociente = 0 #inicialización del contador
while dividendo>=divisor:
	dividendo = dividendo - divisor
	cociente+=1
resto = dividendo
print("El cociente es:",cociente)
print("El resto es:",resto)

