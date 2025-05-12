import numpy as np
import matplotlib.pyplot as plt
# Función para leer la imagen con ruido desde un archivo CSV
def leer_csv(ruta):
    with open(ruta, 'r') as archivo:
        lector_csv = np.loadtxt(archivo, delimiter=',')
    return lector_csv.astype(np.uint8)

# Función para aplicar el filtro de suavizado cuadrado de 3x3
def filtro_suavizado(imagen):
    imagen_suavizada = np.zeros_like(imagen)
    for i in range(1, imagen.shape[0] - 1):
        for j in range(1, imagen.shape[1] - 1):
            vecindad = imagen[i-1:i+2, j-1:j+2]
            suma = np.mean(vecindad)
            imagen_suavizada[i, j] = suma
    return imagen_suavizada
# Función para mostrar la imagen original y la imagen filtrada
def mostrar_imagenes(imagen_original, imagen_filtrada):
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(imagen_original, cmap='gray')
    axs[0].set_title('Imagen original')
    axs[0].axis('off')
    axs[1].imshow(imagen_filtrada, cmap='gray')
    axs[1].set_title('Imagen filtrada')
    axs[1].axis('off')
    plt.show()
# Ruta del archivo CSV que contiene la imagen con ruido
ruta_csv = 'imagen_con_ruido.csv'

# Leer la imagen con ruido desde el archivo CSV
imagen_con_ruido = leer_csv(ruta_csv)

# Aplicar el filtro de suavizado
imagen_filtrada = filtro_suavizado(imagen_con_ruido)
# Mostrar las imágenes lado a lado
mostrar_imagenes(imagen_con_ruido, imagen_filtrada)

# Guardar la imagen filtrada como un archivo CSV
ruta_imagen_filtrada = 'imagen_filtrada.csv'
np.savetxt(ruta_imagen_filtrada, imagen_filtrada, delimiter=',', fmt='%d')

print("Imagen filtrada guardada como:", ruta_imagen_filtrada)