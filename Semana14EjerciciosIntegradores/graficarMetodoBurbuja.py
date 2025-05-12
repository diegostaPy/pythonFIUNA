import numpy as np
import matplotlib.pyplot as plt
import time
# Función de ordenamiento de burbuja
def bubble_sort(arr):
    n = len(arr)
    steps = []
    steps.append(list(arr))
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps.append(list(arr))  # Guardar el estado actual del arreglo en cada paso
    return steps
# Generar un arreglo aleatorio
arr = np.random.randint(1, 100, 10)
# Ordenar el arreglo y obtener los pasos

steps = bubble_sort(arr.copy())
# Configurar el gráfico
plt.figure(figsize=(10, 6))

# Visualizar los pasos del ordenamiento
for i, step in enumerate(steps):
    plt.clf()
    plt.bar(range(len(step)), step, color='skyblue')
    plt.title(f'Paso {i+1}')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.xticks(range(len(step)), [str(x) for x in step])
    plt.ylim(0, 100)
    plt.pause(0.5)  # Pausa para una mejor visualización
    plt.draw()

# Mostrar el gráfico final
plt.show()
