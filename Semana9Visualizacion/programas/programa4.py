try:
    A=int(input())
except ValueError:
    print("debe cargar un numero entero")
try:
    A=int(input())
except Exception as e:
    # Si el archivo no existe, mostramos un mensaje de error
    # Si ocurre cualquier otro tipo de excepción, la manejamos aquí
    print("Se produjo un error inesperado:", e)