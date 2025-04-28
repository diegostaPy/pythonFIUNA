import matplotlib.pyplot as plt

# Intentamos abrir el archivo en modo lectura
with open("programas/datos.txt", "r") as archivo:
    # Leemos el contenido del archivo
    contenido = archivo.readlines()
    # Mostramos el contenido por pantalla
    print("Contenido del archivo:")
print(type(contenido))
for fila in contenido:
    print(fila)
print("el programa llegó aqui")

