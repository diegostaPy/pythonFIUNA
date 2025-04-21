#Diccionarios
tel = {'Juan': 961614098, 'Sapo': 984354139, 'Guido': 973124127, 'Pedro': 981123456}

print(tel['Juan'])





cuadrados = { x: x**2 for x in range(1,11) }
print(tel)
print(cuadrados)

for name, telef in sorted(tel.items()):
    print(name, telef)

for n, sq in cuadrados.items():
    print(f'El cuadrado de {n} es {sq}')

k = tel.keys()
v = tel.values()
print(k)
print(v)
print('------------')
#Tuplas
cliente1 = 123, 'Juan Perez', '0961123456'
cliente2 = 124, 'Luisa Vera', '0985654987'
cliente3 = 125, 'Armando Paredes', '0975894641'

listaClientes = [cliente1, cliente2, cliente3]
for i in listaClientes:
    id, name, tel = i
    print(id, '-', name, ' Telef ', tel) 

#conjuntos
frutas = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'perita', 'banana', 'kiwi'}
print (frutas)
print(sorted(frutas))