# Esta implementación utiliza el pivote como el último elemento en la lista nums
# Tiene un puntero para realizar un seguimiento de los elementos más pequeños que el pivote
# Al final de la función partition(), el puntero se intercambia con el pivote
# para obtener una lista "ordenada" en relación al pivote
import matplotlib.pyplot as plt

# Función para encontrar la posición de partición
def particion(lista, bajo, alto):

    # elegir el elemento más a la derecha como pivote, esto se puede cambiar
    pivote = lista[alto]

    # puntero para el elemento mayor
    i = bajo - 1
    # recorrer todos los elementos
    # comparar cada elemento con el pivote
    for j in range(bajo, alto):
        if lista[j] <= pivote:
            # Si se encuentra un elemento menor que el pivote
            # intercambiarlo con el elemento mayor señalado por i
            i = i + 1
            # Intercambiar el elemento en i con el elemento en j
            (lista[i], lista[j]) = (lista[j], lista[i])
    # Intercambiar el elemento del pivote con el elemento mayor especificado por i
    (lista[i + 1], lista[alto]) = (lista[alto], lista[i + 1])
    # Devolver la posición desde donde se hace la partición
    return i + 1

# función para realizar quicksort
def quickSort(lista, bajo, alto):
    if bajo < alto:
        # Encontrar el elemento pivote de tal manera que
        # los elementos menores que el pivote estén a la izquierda
        # los elementos mayores que el pivote estén a la derecha
        pi = particion(lista, bajo, alto)
        # Llamada recursiva en la parte izquierda del pivote
        quickSort(lista, bajo, pi - 1)
        # Llamada recursiva en la parte derecha del pivote
        quickSort(lista, pi + 1, alto)
     

datos = [1, 7, 4, 1, 10, 9, -2]
print("Lista desordenada:")
print(datos)

tamano = len(datos)

quickSort(datos, 0, tamano - 1)

print('Lista ordenada en orden ascendente:')
print(datos)

