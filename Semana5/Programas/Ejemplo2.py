'''
Generar aleatoriamente las temperaturas (promedio) de todos los días del mes de febrero de 2022 
(entre 30 y 40 grados)y se deben almacenar en el vector tempFeb. 
 Diseñar un programa que obtenga las temperaturas máxima, mínima (e indique los días correspondientes), 
 y el promedio de las que se encuentran entre los días 21 y 27.
'''
#1- Se define y carga la lista
from random import uniform

N = 28
tempFeb=[]
for i in range(N):
    t = uniform(30, 40)
    tempFeb.append(t)

#2- Se determinan los máximos y mínimos
posMax=0 #Posición de la temperatura máxima
posMin=0 #Posición de la temperatura mínima
for i in range(1,N):
    if tempFeb[i]>tempFeb[posMax]:
        posMax=i
    if tempFeb[i]<tempFeb[posMin]:
        posMin=i
print(f"El dia menos caluroso fue el {posMin+1}-Feb con {round(tempFeb[posMin],1)} grados")
print(f"El dia más caluroso fue el {posMax+1}-Feb con {round(tempFeb[posMax],1)} grados")

#3- Se calcula el promedio
suma=0
for i in range(20,27):
    suma+=tempFeb[i]
prom=suma/7
print(f"El promedio de los días 21 al 27 fue de {prom:.2f} grados")
