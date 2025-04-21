import numpy as np
# np.int64: Enteros con signo de 64 bits
int_value = np.int64(10)
print("Tipo de dato: np.int64 - Enteros con signo de 64 bits")
print("Ejemplo:", int_value)
# np.float32: Punto flotante de doble precisión estándar
float_value = np.float32(3.14)
print("\nTipo de dato: np.float32 - Punto flotante de doble precisión estándar")
print("Ejemplo:", float_value)
# np.complex: Números complejos representados por flotantes de 128 bits
complex_value = np.complex128((1, 2))
print("\nTipo de dato: np.complex - Números complejos representados por flotantes de 128 bits")
print("Ejemplo:", complex_value)
# np.bool: Tipo booleano que almacena valores TRUE y FALSE
bool_value = np.bool_(True)
print("\nTipo de dato: np.bool - Tipo booleano que almacena valores TRUE y FALSE")
print("Ejemplo:", bool_value)

# np.string_: Tipo de cadena de longitud fija
string_value = np.string_("Hello")
print("\nTipo de dato: np.string_ - Tipo de cadena de longitud fija")
print("Ejemplo:", string_value)

# np.unicode_: Tipo de unicode de longitud fija
unicode_value = np.unicode_("¡Hola!")
print("\nTipo de dato: np.unicode_ - Tipo de unicode de longitud fija")
print("Ejemplo:", unicode_value)
