import numpy as np
import matplotlib.pyplot as plt
def cargarMat(nombre):
    with open(nombre,'r') as archivo:
        mat=np.loadtxt(archivo,delimiter=',')
    return mat    
def filtrar(mat):
    nfilas,ncolumnas=np.shape(mat)
    matFiltrada=np.empty_like(mat)
    matExtendida=np.zeros((nfilas+2,ncolumnas+2))
    matExtendida[1:-1,1:-1]=mat
    for i in range(0,nfilas+1):
        for j in range(0,ncolumnas+1):
            matFiltrada[i,j]=np.mean(matExtendida[i-1:i+2,j-1:j+2])
    return matFiltrada
mat=cargarMat("imagen_con_ruido.csv")
print(np.shape(mat))
print(np.mean(mat))
print(mat[0:3,0:3])
matFiltrado=filtrar(mat)
plt.imshow(mat, cmap='gray')
plt.show()
np.savetxt("matrizFiltrada.csv",matFiltrado,delimiter=',')