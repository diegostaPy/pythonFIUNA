"""Escribir un programa que solicite al usuario los coeficientes
 a y b de la ecuación de primer grado ax=b, calcule la solución
 e imprima el resultado en pantalla. Obs. asumir que el 
usuario va cargar solamente números(int, float)"""
a=input("Ingrese el valor de a:")
b=input("Ingrese el valor de b:")
af=float(a)
bf=float(b)
if af==0:
    print("La ecuación no tiene solución")
else:
    solucion=bf/af
    print(f"La solución de la ecuación {af}x={bf} es :{solucion}")
print("fin del programa")