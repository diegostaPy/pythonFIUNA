# Lista de ejemplo
mi_lista = ["manzana", "banana", "aguacate","naranja", "uva", "pera"]
# Escribir la lista en el archivo de texto
with open("mi_lista.txt", "w") as f:
    for elemento in mi_lista:
        f.write(elemento + "\n")
#with open("mi_lista.txt","r") as f:
#    print(f.read())
#with open("mi_lista.txt","r") as f:
 #   print(f.readline())
with open("mi_lista.txt","r") as f:
    lista=f.readlines()
print(lista)


"""with open("Planilla_Calificaciones.csv","r") as f:
    print(f.read())
with open("Planilla_Calificaciones.csv","r") as f:
    for linea in f:
        print(linea)
with open("Planilla_Calificaciones.csv","r") as f:
    print(f.readlines())"""