def busqueda_binaria(arr, x):
    izquierda, derecha = 0, len(arr) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        # Si el elemento está en el medio
        if arr[medio] == x:
            return medio
        
        # Si el elemento es mayor, ignoramos la mitad izquierda
        elif arr[medio] < x:
            izquierda = medio + 1
        
        # Si el elemento es menor, ignoramos la mitad derecha
        else:
            derecha = medio - 1
    
    # Si el elemento no está presente en la lista
    return -1

# Ejemplo de uso
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
elemento_a_buscar = 13
resultado = busqueda_binaria(lista, elemento_a_buscar)
if resultado != -1:
    print(f"El elemento {elemento_a_buscar} está presente en el índice {resultado}.")
else:
    print(f"El elemento {elemento_a_buscar} no está presente en la lista.")
