def ordenar_vec_burbuja(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                # Intercambiar A[j] y A[j+1]
                A[j], A[j + 1] = A[j + 1], A[j]

# Ejemplo de uso
A = [64, 34, 25, 12, 22, 11, 90]
ordenar_vec_burbuja(A)
print("Arreglo ordenado:", A)