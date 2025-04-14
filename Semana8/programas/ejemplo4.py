import numpy as np
# Definir los arrays a y b de ejemplo
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[2.5, 2, 3], [7, 2, 3]])
# Resta de dos arrays (a - b)
g = a - b
print("Subtraction:")
print(g)
# Resta de dos arrays usando np.subtract
print("\nSubtraction (np.subtract):")
print(np.subtract(a, b))
# Suma de dos arrays (b + a)
print("\nAddition:")
print(b + a)
# Suma de dos arrays usando np.add
print("\nAddition (np.add):")
print(np.add(b, a))
# División de dos arrays (a / b)
print("\nDivision:")
print(a / b)
# División de dos arrays usando np.divide
print("\nDivision (np.divide):")
print(np.divide(a, b))
# Multiplicación de dos arrays (a * b)
print("\nMultiplication:")
print(a * b)
# Multiplicación de dos arrays usando np.multiply
print("\nMultiplication (np.multiply):")
print(np.multiply(a, b))
print(np.matmul(a,a.transpose()))
# Exponenciación de un array (exp(b))
print("\nExponentiation:")
print(np.exp(b))

# Raíz cuadrada de un array (sqrt(b))
print("\nSquare root:")
print(np.sqrt(b))

# Seno de un array (sin(a))
print("\nPrint sines of an array:")
print(np.sin(a))

# Coseno de un array (cos(b))
print("\nElement-wise cosine:")
print(np.cos(b))

# Logaritmo natural de un array (log(a))
print("\nElement-wise natural logarithm:")
print(np.log(a))

# Producto punto de dos arrays (dot product)
e = np.array([[1, 1], [1, 1]])
f = np.array([[1, 1], [1, 1]])
print("\nDot product:")
print(np.dot(e, f))
