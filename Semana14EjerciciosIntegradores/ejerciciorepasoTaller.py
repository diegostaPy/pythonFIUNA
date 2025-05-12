def xEstaEnLaLista(A, x):
    return x in A
def cargarNumerosDiferentes(A, N):
    contador=0
    while(contador<N):
        n=int(input())
        if n<=N and n>=-N:
            A.append(n)
            contador+=1
def imprimirCombinacionesDe2Elementos(A):
    contador=0
    for x in A:
        contador+=1
        for i in range(contador,len(A)):
            print("["+str(x)+","+str(A[i])+"];",end="")
def sumaRecursiva(A, N):
    pass
def imprimirCombinacionesDe2ElementosQueSumen0(A):
    contador=0
    for x in A:
        contador+=1
        for i in range(contador,len(A)):
            suma=x+A[i]
            if suma==0:
                print("["+str(x)+","+str(A[i])+"];",end="")
# NO MODIFICAR LO QUE ESTA DEBAJO
A = []
opcion = int(input())
N = int(input())
cargarNumerosDiferentes(A, N)
if opcion == 1:
    print(A)
elif opcion == 2:
    imprimirCombinacionesDe2Elementos(A)
elif opcion == 3: