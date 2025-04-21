import matplotlib.pyplot as plt

# Datos para las barras
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [23, 45, 56, 78, 33]

# Crear el gráfico de barras
plt.bar(categorias, valores, color='skyblue')

# Agregar etiquetas y título
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.title('Gráfico de Barras Simple')

# Mostrar el gráfico
plt.show()
