def busqueda_secuencial(arr, x):
    """
    Búsqueda secuencial para encontrar el índice de un elemento en una lista.
    
    :param arr: La lista.
    :param x: El elemento a buscar.
    :return: El índice del elemento en la lista si está presente, de lo contrario, -1.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Ejemplo de uso
lista = [3, 6, 2, 8, 1, 9, 5]
elemento_a_buscar = 8
resultado = busqueda_secuencial(lista, elemento_a_buscar)
if resultado != -1:
    print(f"El elemento {elemento_a_buscar} está presente en el índice {resultado}.")
else:
    print(f"El elemento {elemento_a_buscar} no está presente en la lista.")
