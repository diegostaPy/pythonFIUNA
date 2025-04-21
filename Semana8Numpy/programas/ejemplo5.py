import numpy as np

# Definir los arrays de ejemplo
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[0, 2, 3], [4, 0, 6]])

# Comparaciones Element-wise
print("Comparaciones Element-wise:")
print("a == b:")
print(a == b)
print("\na < 2:")
print(a < a.mean())
print("\nnp.array_equal(a, b):")
print(np.array_equal(a, b))

# Funciones Estadísticas Array-wise
print("\nFunciones Estadísticas Array-wise:")
print("a.sum():", a.sum())
print("a.min():", a.min())
print("b.max(axis=0):", b.max(axis=0))
print("b.cumsum(axis=1):", b.cumsum(axis=1))
print("a.mean():", a.mean())
# print("b.median():", np.median(b)) # No hay función median en numpy
# print("a.corrcoef():", np.corrcoef(a)) # No se puede calcular el coeficiente de correlación con una sola matriz
print("np.std(b):", np.std(b))
