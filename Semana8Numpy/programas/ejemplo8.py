import numpy as np

# Definir los arrays de ejemplo
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = a.copy()
c = a.copy()
d = a.copy()

# Combinar arrays
print("Combinar Arrays:")
print("np.concatenate((a,d),axis=0):")
print(np.concatenate((a,d),axis=0))  # Concatenar arrays verticalmente
print("\nnp.vstack((a,b)):")
print(np.vstack((a,b)))              # Apilar arrays verticalmente (por filas)
print("\nnp.hstack((a,d)):")
print(np.hstack((a,d)))              # Apilar arrays horizontalmente (por columnas)
print("\nnp.column_stack((a,d)):")
print(np.column_stack((a,d)))        # Crear arrays apilados por columnas
print("\nnp.c_[a,d]:")
print(np.c_[a,d])                    # Crear arrays apilados por columnas

# Dividir arrays
print("\nDividir Arrays:")
print("np.hsplit(a,3):")
print(np.hsplit(a,3))                # Dividir el array horizontalmente
print("\nnp.vsplit(c,2):")
print(np.vsplit(c,2))                # Dividir el array verticalmente
