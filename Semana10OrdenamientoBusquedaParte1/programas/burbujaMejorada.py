def ordenar_vec_burbuja_mejora(A):
    n = len(A)
    i = 0
    continuar = True
    while continuar:
        continuar = False
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                # Intercambiar A[j] y A[j+1]
                A[j], A[j + 1] = A[j + 1], A[j]
                continuar = True
        i += 1

# Ejemplo de uso
A = [64, 34, 25, 12, 22, 11, 90]
ordenar_vec_burbuja_mejora(A)
print("Arreglo ordenado:", A)