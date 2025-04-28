import numpy as np
import matplotlib.pyplot as plt
# Generar 1000 números aleatorios distribuidos uniformemente entre 0 y 100
numeros_aleatorios = np.random.uniform(0, 100, 1000)
print(numeros_aleatorios)
# Crear el histograma
fig, ax = plt.subplots()  

plt.hist(numeros_aleatorios, bins=(0,50,100), color='skyblue', edgecolor='black')
# Agregar etiquetas y título
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma de Números Aleatorios')
# Mostrar el histograma
plt.show()
fig.savefig("histograma.png")