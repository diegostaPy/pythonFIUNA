import numpy as np
zeros_array = np.zeros((3,4,5))
print("Arreglo de ceros:")
print(zeros_array)
ones_array = np.ones((3,4), dtype=np.int16)
print("\nArreglo de unos:")
print(ones_array)
d = np.arange(10,25,5)
print("\nArreglo con valores equiespaciados (con paso):")
print(d)
linspace_array = np.linspace(0,2,9)
print("\nArreglo con valores equiespaciados (número de muestras):")
print(linspace_array)
constant_array = np.full((2,2),7)
print("\nArreglo constante:")
print(constant_array)

# Crear una matriz identidad
identity_matrix = np.eye(2)
print("\nMatriz identidad:")
print(identity_matrix)

# Crear un arreglo con valores aleatorios
random_array = np.random.randint(0,100,size=(2,2))
print("\nArreglo con valores aleatorios:")
print(random_array)

# Crear un arreglo vacío
empty_array = np.empty((3,2))
print("\nArreglo vacío:")
print(empty_array)
