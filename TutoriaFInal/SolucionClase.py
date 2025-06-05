import numpy as np
import matplotlib.pyplot as plt
# ingenieria electronica
def validar(a=0):
    x=-1
    while x < a or x > 10:
        x=float(input(f"Ingrese un número entre {a} y 10: "))
        if x < a or x > 10:
            print(f"Número no válido. Debe estar entre {a} y 10.")
    return x   
def funcion(x,w0=1):
    return 1 / (1 + (x / w0)**2)**(1/2)
def integral_montecarlo(a,b,N):
    x = np.random.uniform(a, b, N)
    y = np.random.uniform(0, 1, N)
    debajo_curva = y < funcion(x)
    return (b - a) * np.sum(debajo_curva) / N
def graficar(N=1000, a=0, b=10):
    X = np.linspace(a, b, 100)
    Y = funcion(X)
    plt.plot(X, Y,"-.", label='Función Electrónica')
    x = np.random.uniform(a, b, N)
    y = np.random.uniform(0, 1, N)
    debajo_curva = y < funcion(x)
    plt.scatter(x[debajo_curva], y[debajo_curva], color='red', s=1, label='Debajo de la curva')
    plt.scatter(x[~debajo_curva], y[~debajo_curva], color='green', s=1, label='Encima de la curva')
            
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud')
    plt.title('Respuesta en Frecuencia')
    plt.legend()
    plt.grid()
    plt.show()

a= validar()
print(f"El número ingresado es: {a}")
b= validar(a=a)
print(f"El número ingresado es: {b}")
N_values = [10, 50, 100, 250, 500, 1000,10000]
areas = []
for N in N_values:
    area = integral_montecarlo(a, b, N)
    areas.append(area)
    print(f"Área estimada con N={N}: {area}")
graficar()





