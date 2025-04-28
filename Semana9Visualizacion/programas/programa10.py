import numpy as np
import matplotlib.pyplot as plt

# Generar datos
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Crear el gráfico de líneas con diferentes estilos
plt.plot(x, y1, color='blue', linestyle=':', linewidth=2, label='Sen(x)')  # Línea sólida azul
plt.plot(x, y2, color='red', linestyle='--', linewidth=2, label='Cos(x)')  # Línea discontinua roja

# Agregar marcadores a algunos puntos
plt.plot(x[::10], y1[::10], marker='o', color='green', markersize=8, linestyle='', label='Marcadores Sen(x)')  # Círculos verdes
plt.plot(x[::10], y2[::10], marker='s', color='purple', markersize=8, linestyle='', label='Marcadores Cos(x)')  # Cuadrados morados

# Agregar etiquetas y título
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de Líneas con Marcadores')
plt.legend()

# Mostrar el gráfico
plt.show()
