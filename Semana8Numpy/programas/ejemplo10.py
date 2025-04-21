import numpy as np

# Leer archivo CSV con NumPy
datos = np.genfromtxt('Planilla_Calificaciones.csv', delimiter=',')

print("Datos leídos del archivo CSV:")
print(datos)

# Escribir datos en un nuevo archivo CSV
nuevo_archivo = 'datos_nuevos.csv'
np.savetxt(nuevo_archivo, datos, delimiter=',')

print("\nDatos escritos correctamente en el archivo:", nuevo_archivo)


