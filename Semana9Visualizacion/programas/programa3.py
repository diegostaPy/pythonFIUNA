import numpy as np

try:
    # Intentamos cargar los datos desde el archivo "datos.txt"
    datos = np.loadtxt("datos.txt")
    # Si la carga es exitosa, mostramos los datos por pantalla
    print("Datos cargados exitosamente:")
    print(datos)
except FileNotFoundError:
    # Si el archivo no existe, mostramos un mensaje de error
    print("El archivo no existe.")
except ValueError:
    # Si hay un error al cargar los datos, mostramos un mensaje de error
    print("Error al cargar los datos. Asegúrate de que el archivo tenga el formato correcto.")
except Exception as e:
    # Si ocurre cualquier otro tipo de excepción, la manejamos aquí
    print("Se produjo un error inesperado:", e)
