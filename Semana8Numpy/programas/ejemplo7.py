import numpy as np

# Definir los arrays de ejemplo
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([[1.5, 2, 3],
              [1, 2, 3],
              [4, 5, 6]])
c = np.array([[[1.5, 2, 1],
               [4, 5, 6]],
              [[3, 2, 3],
               [4, 5, 6]]])
d = np.array([[10, 15, 20]])

# Transponer un array
print("Transponiendo un Array:")
i = np.transpose(b)
print("np.transpose(b):")
print(i)
print("i.T:")
print(i.T)
print()

# Cambiando la forma de un array
print("Cambiando la Forma de un Array:")
print("b.ravel():", b.ravel())                 # Aplanar el array
print("g.reshape(3,-2):", b.reshape(3, -2))     # Reorganizar el array sin cambiar los datos
print()

# Añadir/Quitar elementos de un array
print("Añadir/Quitar elementos de un Array:")
h = np.array([[1, 2, 3],
              [4, 5, 6]])
print("h.resize((2,6)):", h.resize((2,6)))      # Cambiar la forma del array

# Combinar arrays
print("Combinar Arrays:")
print("np.concatenate((a,d),axis=0):", np.concatenate((a,d),axis=0)) # Concatenar arrays

A=np.array([1,2,3])
B=np.array([4,5,6])
C=np.hstack((A,B))
print(C)
print(C.shape)
print(C.ndim)
print(A.reshape(-1,1))