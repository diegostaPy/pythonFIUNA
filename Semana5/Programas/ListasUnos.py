import random
lista = []
n = 12 #se puede leer por teclado
for i in range(n):
    lista.append(random.randint(0,1))

print(lista)
nueva_lista = []
#lista = [1,0,1, 0,0,0, 1,0,0, 1,1,1, 0,0,1]
for i in range(0, len(lista), 3):
    sublista = lista[i:i + 3]
    nueva_lista.extend(sublista)
    
    unos = sublista.count(1)
    nueva_lista.append(unos)

print(nueva_lista)