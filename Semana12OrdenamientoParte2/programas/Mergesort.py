def merge(izquierda, derecha, arr):
    i = j = k = 0

    # Fusionar las dos mitades
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            arr[k] = izquierda[i]
            i += 1
        else:
            arr[k] = derecha[j]
            j += 1
        k += 1

    # Comprobar si quedan elementos en alguna de las mitades
    while i < len(izquierda):
        arr[k] = izquierda[i]
        i += 1
        k += 1

    while j < len(derecha):
        arr[k] = derecha[j]
        j += 1
        k += 1

def merge_sort(arr):
    if len(arr) > 1:
        medio = len(arr) // 2
        izquierda = arr[:medio]
        derecha = arr[medio:]

        print("División:", arr)
        print("Izquierda:", izquierda)
        print("Derecha:", derecha)

        merge_sort(izquierda)
        merge_sort(derecha)

        merge(izquierda, derecha, arr)
        print("Fusión intermedia:", arr)

# Ejemplo de uso
datos = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", datos)
print("Iniciando Merge Sort:")
merge_sort(datos)
print("Lista ordenada:", datos)

