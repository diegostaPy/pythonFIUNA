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
    n=int(parte_numerica)
    invertido=0
    while n>0:
        invertido=invertido*10+n%10
        n=int(n/10)
    print(signo + str(invertido))
else:
    print("Error: entrada no válida")
