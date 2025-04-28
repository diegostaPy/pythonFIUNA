import numpy as np
import matplotlib.pyplot as plt

# Generar una matriz aleatoria de 10x10
matriz = np.random.rand(10, 10)
#matriz = np.array([[i + j for i in range(10)] for j in range(10)])
# Visualizar la matriz utilizando imshow
plt.imshow(matriz, cmap='viridis')
# Agregar barra de color
plt.colorbar()
# Mostrar la imagen
plt.show()
