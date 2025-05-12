import numpy as np
import matplotlib.pyplot as plt

# Función de ordenamiento de burbuja
def ordenamiento_burbuja(arr):
    n = len(arr)
    pasos = []
    pasos.append(list(arr)) # Guardar el estado inicial del arreglo
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                pasos.append(list(arr))  # Guardar el estado actual del arreglo en cada paso
    return pasos

# Generar un arreglo aleatorio
arr = np.random.randint(1, 100, 12)
# Ordenar el arreglo y obtener los pasos
pasos = ordenamiento_burbuja(arr.copy())
# Configurar el gráfico
plt.figure(figsize=(10, 6))

# Visualizar los pasos del ordenamiento
for i, paso in enumerate(pasos): #enumerate añade un contador a un iterable (en este caso, lista), y con ello se puede tener (en cada iteración) el índice del elemento y el elemento mismo
    plt.clf()
    plt.bar(range(len(paso)), paso, color='skyblue')
    plt.title(f'Paso {i+1}')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.xticks(range(len(paso)), [str(x) for x in paso])
    plt.ylim(0, 100)
    plt.pause(0.5)  # Pausa para una mejor visualización
    plt.draw()

# Mostrar el gráfico final
plt.show()