numero = input()

# Validar si es un número entero (positivo o negativo)
if numero.startswith("-"):
    parte_numerica = numero[1:]
    signo = "-"
else:
    parte_numerica = numero
    signo = ""

if parte_numerica.isdigit():
    # Invertir los dígitos manualmente
    invertido = ""
    for digito in parte_numerica:
        invertido = digito + invertido

    # Eliminar ceros a la izquierda
    invertido_sin_ceros = invertido.lstrip("0")
    if invertido_sin_ceros == "":
        invertido_sin_ceros = "0"

    print(signo + invertido_sin_ceros)
else:
    print("Error: entrada no válida")
