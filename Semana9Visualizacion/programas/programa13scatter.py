import numpy as np
import matplotlib.pyplot as plt
# Generar datos para una relación lineal y agregar ruido aleatorio
np.random.seed(0)
x = np.linspace(0, 10, 100)
y1 = 2 * x + 1 + np.random.normal(0, 1, 100)  # Relación lineal y ruido
y2 = 2 * x + 1 + np.random.normal(0, 3, 100)  # Relación lineal y ruido

# Crear el gráfico de dispersión
plt.scatter(x, y1,s=0.5, color='blue', alpha=0.7)
plt.scatter(x, y2,s=1.5, color='red', alpha=0.7)

# Agregar etiquetas y título
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Gráfico de Dispersión con Relación Lineal')

# Mostrar el gráfico
plt.show()
