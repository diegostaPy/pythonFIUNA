while True:
    try:
        # Solicitamos al usuario que ingrese un número entero
        numero = int(input("Ingrese un número entero: "))
        # Si la conversión a entero es exitosa, salimos del bucle
        break
    except ValueError:
        # Si ocurre un error al convertir a entero (por ejemplo, si el usuario ingresa una cadena no numérica),
        # mostramos un mensaje de error y continuamos solicitando al usuario que ingrese un número.
        print("Error: Por favor, ingrese un número entero válido.")

# Una vez que se sale del bucle, significa que se ha ingresado un número entero válido.
print("El número entero ingresado es:", numero)