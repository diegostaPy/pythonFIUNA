import numpy as np
import matplotlib.pyplot as plt
def cargarMat(nombre):
    with open(nombre,'r') as archivo:
        mat=np.loadtxt(archivo,delimiter=',')
    return mat    
def filtrar(mat):
    nfilas,ncolumnas=np.shape(mat)
    matFiltrada=np.empty_like(mat)
    for i in range(1,nfilas):
        for j in range(1,ncolumnas):
            matFiltrada[i,j]=np.mean(mat[i-1:i+2,j-1:j+2])
    return matFiltrada
mat=cargarMat("imagen_con_ruido.csv")
print(np.shape(mat))
print(np.mean(mat))
print(mat[0:3,0:3])
matFiltrado=filtrar(mat)
plt.imshow(mat, cmap='gray')
plt.show()
np.savetxt("matrizFiltrada.csv",matFiltrado,delimiter=',',fmt="%d")