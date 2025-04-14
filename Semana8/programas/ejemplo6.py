import numpy as np

# Crear un array de ejemplo
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Subconjuntos
print("Subconjuntos:")
print("arr[0]:", arr[0])             # Primer fila
print("arr[:, 1]:", arr[:, 1])       # Segunda columna
print("arr[1, 1:]:", arr[1, 1:])     # Desde la segunda columna hasta el final de la segunda fila
print()

# Segmentación
print("Segmentación:")
print("arr[:2, :2]:", arr[:2, :2])   # Subarray de las primeras dos filas y columnas
print("arr[1:, 1:]:", arr[1:, 1:])   # Subarray desde la segunda fila hasta el final y desde la segunda columna hasta el final
print()

# Indexación booleana
print("Indexación booleana:")
mask = arr > 5                       # Crear una máscara booleana para valores mayores que 5
print("Mask:")
print(mask)
print("arr[mask]:", arr[mask])       # Seleccionar elementos que cumplan con la máscara
