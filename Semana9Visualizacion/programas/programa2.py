Bandera=True
nombreArchivo="datos.txt"
while(Bandera):
    try:
        # Intentamos abrir el archivo en modo lectura
        with open(nombreArchivo, "r") as archivo:
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)
            Bandera=False
    except FileNotFoundError:
        # Si el archivo no existe, mostramos un mensaje de error
        print("El archivo no existe.")
        nombreArchivo=input("Ingrese Nuevamente el nombre deç archivo:")

print("el programa llegó aqui")

