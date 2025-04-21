try:
    # Intentamos abrir el archivo en modo lectura
    with open("desktop.ini", "r") as archivo:
        # Leemos el contenido del archivo
        contenido = archivo.read()
        # Mostramos el contenido por pantalla
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    # Si el archivo no existe, mostramos un mensaje de error
    print("El archivo no existe.")

print("el programa llegó aqui")

