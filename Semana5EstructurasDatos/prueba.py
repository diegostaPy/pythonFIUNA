n=int(input( ))
lista=[]
suma=0
positivos=0

for i in range(n):
    numero=int(input( ))
    lista.append(numero)
    if numero > 0:
        suma += numero
        positivos += 1

promedio=suma/positivos
promedio_truncado=int(promedio*100)/100

print(lista)
print(f"La suma es {suma}")
print(f"El promedio es {promedio_truncado}")
print(f"El promedio es {promedio}")