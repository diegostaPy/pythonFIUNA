def ordenar_vec_insercion(A):
    n = len(A)
    for i in range(1, n):
        aux = A[i]
        pos_encontrada = False  # indica si ya se encontró la posición del nuevo elemento
        j = i - 1
        while j >= 0 and not pos_encontrada:
            if A[j] > aux:
                # Se desplaza a la derecha
                A[j + 1] = A[j]
                j -= 1
            else:
                pos_encontrada = True
        # Se coloca el nuevo elemento
        A[j + 1] = aux

# Ejemplo de uso
A = [5,3,6,2,1,4]
ordenar_vec_insercion(A)
print("Arreglo ordenado:", A)