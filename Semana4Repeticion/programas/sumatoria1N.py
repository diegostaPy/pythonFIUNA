#Sumatoria de 1 hasta n
n=int(input())
sumatoria=0
factorial=1
for i in range(n):
    i=i+1
    factorial=factorial*i
    sumatoria=sumatoria+factorial
    
print("La sumatoria de factorial de n es", sumatoria)
print("El de factorial de n es", factorial)