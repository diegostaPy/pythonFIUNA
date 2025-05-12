from PIL import Image
import numpy as np
import csv

# Función para leer la imagen PNG y convertirla en una matriz de intensidades
def leer_imagen(ruta):
    imagen = Image.open(ruta).convert('L')  # Convertir la imagen a escala de grises
    matriz = np.array(imagen)
    return matriz

# Función para agregar ruido a la imagen
def agregar_ruido(imagen, nivel=60):
    ruido = np.random.normal(0, nivel, imagen.shape)
    imagen_con_ruido = imagen + ruido
    imagen_con_ruido = np.clip(imagen_con_ruido, 0, 255)  # Asegurar que los valores estén en el rango válido
    return imagen_con_ruido.astype(np.uint8)

# Función para guardar la matriz de intensidades en un archivo CSV
def guardar_csv(matriz, ruta):
    with open(ruta, 'w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(matriz)

# Ruta de la imagen PNG
ruta_imagen = 'gamagrafia.png'

# Leer la imagen y convertirla en una matriz de intensidades
imagen_original = leer_imagen(ruta_imagen)

# Agregar ruido a la imagen
imagen_con_ruido = agregar_ruido(imagen_original)

# Guardar la imagen con ruido como un archivo CSV
ruta_csv = 'imagen_con_ruido.csv'
guardar_csv(imagen_con_ruido, ruta_csv)

print("Imagen con ruido guardada como archivo CSV:", ruta_csv)
