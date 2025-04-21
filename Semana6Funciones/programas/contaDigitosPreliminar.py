import math

#Función que devuelve el resultado de a^b.
#Se supone que b es un número no-negativo.*/
def potencia(a, b):
    return a**b

#Función que devuelve true si el número n es primo, y false en caso contrario.
#Se supone que n es positivo.*/
def esPrimo(n):
    for i in range(2,int(n/2)):
        if(n%i==0):
            return False
    return True
def esPrimov2(n):
    resultado=True
    for i in range(2,n/2):
        if(n%i==0):
            resultado=False
            break
            
    return resultado
            
#Función que devuelve la cantidad de dígitos de un número n.
#Se supone que n es positivo.*/
def cantDigitos(n):
    return int(math.log10(n))+1
def cantDigitosV2(n):
    cont=0
    while(n>0):
        cont=cont+1
        n=int(n/10)
    return cont
    

def cantNoPrimos_C_Digitos(N,C):
    nd=cantDigitos(N)
    n=N
    cont=0
    while n>0:
        digito=N%10
        if(not(esPrimo(digito))):
            cont+=1
        n=int(n/10)
        
    return cont
    

N=int(input())
C=int(input())

print("Cantidad de no-primos de ",C," digitos: ",cantNoPrimos_C_Digitos(N,C))