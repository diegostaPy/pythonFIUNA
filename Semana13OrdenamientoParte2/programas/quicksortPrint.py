import numpy as np
def mediana_de_tres(lista, bajo, alto):
    opciones = [lista[bajo], lista[(bajo + alto) // 2], lista[alto]]
    pivote_index = np.argsort(opciones)[1]  
    # Índice del segundo elemento después de ordenar
    return pivote_index
def particion(lista, bajo, alto):
    # Explicación de la partición
    print(f"Paso de partición: Lista = {lista}, bajo = {bajo}, alto = {alto}")

    # Elegir el pivote como el último elemento
    pivote = lista[mediana_de_tres(lista, bajo, alto)]#lista[alto]
    print(f"Pivote seleccionado: {pivote}")

    # Inicializar el puntero para los elementos más pequeños que el pivote
    i = bajo - 1

    # Recorrer la lista y comparar cada elemento con el pivote
    for j in range(bajo, alto):
        if lista[j] <= pivote:
            # Incrementar el puntero
            i += 1
            # Intercambiar el elemento actual con el elemento señalado por el puntero
            lista[i], lista[j] = lista[j], lista[i]
            print(f"Intercambiando {lista[i]} con {lista[j]} => {lista}")

    # Intercambiar el pivote con el elemento señalado por el puntero
    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
    print(f"Intercambiando {lista[i + 1]} con pivote {pivote} => {lista}")

    # Devolver el índice del pivote
    return i + 1

def quickSort(lista, bajo, alto):
    if bajo < alto:
        # Particionar la lista
        pi = particion(lista, bajo, alto)
        print(f"Lista después de la partición: {lista}")

        # Llamada recursiva a quickSort para las sublistas izquierda y derecha del pivote
        print("Recursión a la izquierda")
        quickSort(lista, bajo, pi - 1)
        print("Recursión a la derecha")
        quickSort(lista, pi + 1, alto)

# Ejemplo de uso
arr = np.random.randint(1, 100, 10)
datos =list(arr)
print("Lista original:", datos)
print("Iniciando Quicksort")
quickSort(datos, 0, len(datos) - 1)
print("Lista ordenada:", datos)
