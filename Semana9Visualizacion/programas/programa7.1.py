import matplotlib.pyplot as graficar
# Crear figura y ejes
fig, ax = graficar.subplots()
# Graficar datos
ax.plot([1, 2, 3, 4], [1, 4, 2, 3],'r+')
ax.plot( [3, 2, 3, 2],'bo')

# Agregar etiquetas y título
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Gráfico de Líneas')
# Mostrar el gráfico
graficar.show()
fig.savefig("grafico1.png",dpi=300)
