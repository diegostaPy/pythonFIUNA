import random
import time

def ordenamiento_Seleccion(A):
    N = len(A)
    for i in range(N):
        pos = i
        for j in range(i+1,N):
            if A[j]<A[pos]:
                pos=j
        #Intercambio
        A[i],A[pos] = A[pos],A[i]

def ordenamiento_Insercion(A):
    N = len(A)
    for i in range(1,N):
        elem = A[i]
        j=i-1
        while j>=0 and A[j]>elem:
            #El elemento en A[j] se desplaza un lugar a la derecha
            A[j+1] = A[j]
            j=j-1
        #Se coloca el "nuevo" elemento en su lugar respectivo
        A[j+1] = elem

def ordenamiento_Burbuja_Mejorada(A):
    N = len(A)
    continuar=True
    while continuar:
        continuar=False
        for j in range(N-i-1):
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j] #tuplas
                continuar=True

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

def ordenamiento_MergeSort(A):
    '''
    Para la primera llamada a la función recursiva
    '''
    mergeSortRec(A,0,len(A)-1)

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

def ordenamiento_QuickSort(A):
    '''
    Para la primera llamada a la función recursiva
    '''
    quicksortRec(A,0,len(A)-1)

'''
El proceso es el siguiente:
    - Se generan, de manera aleatoria, N listas de tamaño "tam".
    - Cada uno de estos vectores se ordena mediante cada método de ordenamiento, contando el tiempo respectivo.
    - Se muestran al final los tiempos totales de ejecucion para cada método.
'''
tam=500
N=10

#Inicializacion de acumuladores
tSel=0
tIns=0
tBur=0
tMer=0
tQui=0
tpython=0
#Impresion de datos de la prueba
print("Comparacion de metodos de ordenamiento\n")
print("Datos:")
print("Tamanho del vector:",tam)
print("Numero de repeticiones:",N)

#Proceso principal
A = [0]*tam
print("Caso: ",end="")
for k in range(N):
    print(k,end=' ')
    #Se genera un vector de manera aleatoria
    for i in range(tam):
        A.append(random.randint(1,1000))

    #Método de selección
    #Se copian los elementos de A a B, para que todos los metodos utilicen el mismo vector
    B = A[:]
    inicio = time.time()
    ordenamiento_Seleccion(B)
    fin = time.time()
    tSel+=(fin-inicio)

    #Método de inserción
    B = A[:]
    inicio = time.time()
    ordenamiento_Insercion(B)
    fin = time.time()
    tIns+=(fin-inicio)

    #Método de burbuja
    B = A[:]
    inicio = time.time()
    ordenamiento_Burbuja_Mejorada(B)
    fin = time.time()
    tBur+=(fin-inicio)

    #Método Mergesort
    B = A[:]
    inicio = time.time()
    ordenamiento_MergeSort(B)
    fin = time.time()
    tMer+=(fin-inicio)

    #Método Quicksort
    B = A[:]
    inicio = time.time()
    ordenamiento_QuickSort(B)
    fin = time.time()
    tQui+=(fin-inicio)
    #Método python
    B = A[:]
    inicio = time.time()
    B.sort()
    fin = time.time()
    tpython+=(fin-inicio)
#Impresión de resultados
print("\n\nResultados - Tiempos totales de ejecución:")
print("Selección:",tSel)
print("Inserción:",tIns)
print("Burbuja:",tBur)
print("Mergesort:",tMer)
print("Quicksort:",tQui)

print("python:",tpython)

