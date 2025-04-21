import matplotlib.pyplot as plt
# Crear figura y ejes
fig, ax = plt.subplots()
# Graficar datos
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
# Agregar etiquetas y título
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Gráfico de Líneas')
# Mostrar el gráfico
#plt.show()
fig.savefig("grafico1.png",dpi=300)
