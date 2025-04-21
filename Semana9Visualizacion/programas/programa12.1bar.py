import matplotlib.pyplot as plt

# Datos para las barras
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [23, 45, 56, 78, 33]

# Crear el gráfico de barras
plt.bar(categorias, valores, color='skyblue', edgecolor='black', linewidth=2, width=0.6, align='center')

# Agregar etiquetas y título
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.title('Gráfico de Barras Personalizado')

# Mostrar el gráfico
plt.show()
