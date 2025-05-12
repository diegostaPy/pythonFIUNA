
# por longitud
lista = ["perro", "gato", "elefante", "ratón"]
lista_ordenada = sorted(lista, key=len)
print(lista_ordenada)  # Salida: ['gato', 'perro', 'ratón', 'elefante']
# por funciones lambda
lista = [(2, 'b'), (1, 'a'), (3, 'c')]
lista.sort(key=lambda x: x[1])
print(lista)  # Salida: [(1, 'a'), (2, 'b'), (3, 'c')]

#ordenamiento por llaves
def prueba(datos):
    return datos['Matemáticas']

estudiantes = [
    {'Nombre': 'Juan Perez', 'Matemáticas': 99},
    {'Nombre': 'Jose Colbes', 'Matemáticas': 100},
    {'Nombre': 'Diego Stalder', 'Matemáticas': 97},
    {'Nombre': 'Luis Gonzalez', 'Matemáticas': 98},
    {'Nombre': 'Pedro Torres', 'Matemáticas': 99}
]

print("Lista original de estudiantes:")
print(estudiantes)

estudiantes.sort(key=prueba)

print("\nLista de estudiantes después de ordenar por calificaciones en Matemáticas:")
print(estudiantes)

