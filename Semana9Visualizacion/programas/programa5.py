try:
    # Solicitamos al usuario que ingrese un número entero
    numero = int(input("Ingrese un número entero: "))
except ValueError as ve:
    # Si se produce un ValueError (por ejemplo, si el usuario ingresa una cadena en lugar de un número),
    # mostramos un mensaje de error
    print("Error:", ve)
else:
    # Si no se produce ninguna excepción, es decir, el número ingresado es válido,
    # mostramos un mensaje indicando que el número es válido
    print("El número ingresado es:", numero)
finally:
    # La cláusula finally se ejecuta siempre, independientemente de si se produce una excepción o no.
    # Aquí podemos realizar limpieza de recursos o cualquier acción que deba realizarse
    # independientemente del resultado del bloque try-except.
    print("Ejecución finalizada.")
