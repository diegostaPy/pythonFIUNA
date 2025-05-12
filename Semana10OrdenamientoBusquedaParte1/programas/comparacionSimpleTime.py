import time

# Implementación de los métodos de ordenamiento

def ordenar_vec_burbuja(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

def ordenar_vec_seleccion(A):
    n = len(A)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if A[j] < A[min_idx]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]

def ordenar_vec_insercion(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >=0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

# Generar listas de diferentes longitudes
listas = []
for i in range(100, 1100, 100):
    listas.append(list(range(i, 0, -1)))  # Lista en orden inverso

# Comparar métodos de ordenamiento
for lista in listas:
    print(f"\nTamaño de lista: {len(lista)}")
    for metodo in [ordenar_vec_burbuja, ordenar_vec_seleccion, ordenar_vec_insercion, sorted]:
        lista_copy = lista.copy()  # Hacer una copia de la lista original
        start_time = time.time()  # Tiempo de inicio
        metodo(lista_copy)  # Ordenar la lista
        end_time = time.time()  # Tiempo de fin
        elapsed_time = end_time - start_time  # Tiempo transcurrido
        print(f"{metodo.__name__}: {elapsed_time:.6f} segundos")
