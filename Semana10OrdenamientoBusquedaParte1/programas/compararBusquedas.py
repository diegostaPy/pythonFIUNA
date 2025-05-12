import time

def busqueda_secuencial(arr, x):
    """
    Búsqueda secuencial para encontrar el índice de un elemento en una lista.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def busqueda_binaria(arr, x):
    """
    Búsqueda binaria para encontrar el índice de un elemento en una lista ordenada.
    """
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == x:
            return medio
        elif arr[medio] < x:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Ejemplo de búsqueda usando index()
def busqueda_con_index(arr, x):
    """
    Búsqueda utilizando el método index() de las listas.
    """
    try:
        indice = arr.index(x)
        return indice
    except ValueError:
        return -1

# Lista de ejemplo
lista = list(range(1, 1000001))  # Lista de números del 1 al 1000000

# Elemento a buscar
elemento = 999999

# Medir tiempo de búsqueda secuencial
start_time = time.time()
indice_secuencial = busqueda_secuencial(lista, elemento)
end_time = time.time()
tiempo_secuencial = end_time - start_time

# Medir tiempo de búsqueda binaria
start_time = time.time()
indice_binaria = busqueda_binaria(lista, elemento)
end_time = time.time()
tiempo_binaria = end_time - start_time

# Medir tiempo de búsqueda con index()
start_time = time.time()
indice_index = busqueda_con_index(lista, elemento)
end_time = time.time()
tiempo_index = end_time - start_time

# Imprimir resultados
print(f"Resultado de la búsqueda secuencial: {indice_secuencial}, Tiempo: {tiempo_secuencial} segundos")
print(f"Resultado de la búsqueda binaria: {indice_binaria}, Tiempo: {tiempo_binaria} segundos")
print(f"Resultado de la búsqueda con index(): {indice_index}, Tiempo: {tiempo_index} segundos")
