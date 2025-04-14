import numpy as np
# Generar datos aleatorios
datos_aleatorios = np.random.randint(0, 100, size=(5, 3))
print("Datos aleatorios generados:")
print(datos_aleatorios)
# Guardar los datos en un archivo CSV
nombre_archivo = 'datos_aleatorios.csv'
np.savetxt(nombre_archivo, datos_aleatorios, delimiter=',', fmt='%d')
print("\nDatos guardados correctamente en el archivo:", nombre_archivo)
# Cargar datos desde el archivo 
datos = np.loadtxt('datos_aleatorios.csv' , delimiter=",")
print("Datos cargados desde el archivo:")
print(datos)