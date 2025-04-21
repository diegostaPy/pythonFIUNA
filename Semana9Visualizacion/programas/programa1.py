import matplotlib.pyplot as plt

# Intentamos abrir el archivo en modo lectura
with open("datos.txt", "r") as archivo:
    # Leemos el contenido del archivo
    contenido = archivo.read()
    # Mostramos el contenido por pantalla
    print("Contenido del archivo:")
    print(contenido)

print("el programa llegó aqui")

