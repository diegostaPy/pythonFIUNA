import numpy as np
import matplotlib.pyplot as plt
# Generar valores x desde 0 a 2*pi con paso de 0.1
x = np.arange(0, 2*np.pi, 0.1)
# Calcular los valores y correspondientes utilizando la función seno
y = np.sin(x)
# Crear el gráfico de líneas
plt.plot(x, y)
# Agregar etiquetas y título
plt.xlabel('X')
plt.ylabel('Sen(X)')
plt.title('Gráfico de la Función Seno')

# Mostrar el gráfico
plt.show()
