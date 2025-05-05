import random

def mezclar(A,p,q,r):
    '''
    Función que implementa la mezcla o fusión
    '''
    n1 = q-p+1
    n2 = r-q
    L=[]
    for i in range(n1):
        L.append(A[p+i])
    R=[]
    for i in range(n2):
        R.append(A[q+i+1])
    i=0
    j=0
    for k in range(p,r+1):
        if L[i]<=R[j]: #se toma un elemento de L
            A[k]=L[i]
            i+=1
        else: #se toma un elemento de R
            A[k]=R[j] 
            j+=1
        if i==len(L): #se llegó al final del arreglo L
            for m in range(k+1,r+1):
                A[m]=R[j]
                j+=1
            break
        if j==len(R): #se llegó al final del arreglo R
            for m in range(k+1,r+1):
                A[m]=L[i]
                i+=1
            break

def mergeSortRec(A,p,r):
    '''
    Función recursiva que realiza el MergeSort de A desde p hasta r
    '''
    if p<r:
        q=(p+r)//2
        mergeSortRec(A,p,q)
        mergeSortRec(A,q+1,r)
        mezclar(A,p,q,r)

def mergeSort(A):
    '''
    Para la primera llamada a la función recursiva
    '''
    mergeSortRec(A,0,len(A)-1)

N=10 #cantidad de elementos a considerar
lista=[]
for i in range(N):
    lista.append(random.randint(1,N)) #generamos valores aleatorios entre 1 y N
print("Lista antes del ordenamiento:",lista)
mergeSort(lista)
print("Lista luego del ordenamiento:",lista)
