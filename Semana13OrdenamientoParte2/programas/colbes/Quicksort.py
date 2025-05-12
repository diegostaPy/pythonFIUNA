import random

def particion(A,p,r):
    '''
    Función que realiza la partición, tomando el primer elemento del bloque [p,r] como pivot
    '''
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def quicksortRec(A,p,r):
    '''
    Función recursiva que realiza el MergeSort de A desde p hasta r
    '''
    if p<r:
        q=particion(A,p,r)
        quicksortRec(A,p,q-1)
        quicksortRec(A,q+1,r)

def quickSort(A):
    '''
    Para la primera llamada a la función recursiva
    '''
    quicksortRec(A,0,len(A)-1)

N=10 #cantidad de elementos a considerar
lista=[]
for i in range(N):
    lista.append(random.randint(1,N)) #generamos valores aleatorios entre 1 y N
print("Lista antes del ordenamiento:",lista)
quickSort(lista)
print("Lista luego del ordenamiento:",lista)
