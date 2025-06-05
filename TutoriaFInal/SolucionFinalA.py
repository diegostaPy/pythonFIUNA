import numpy as np  
def validar():
    x=input("Ingrese la posición actual de la Torre ")
    while(len(x)!=2 or ord(x[0])<ord('a') or ord(x[0])>ord('h') or int(x[1])<1 or int(x[1])>8):
        print("Posición no válida. Debe ser una letra entre 'a' y 'h' seguida de un número entre 1 y 8.")
        x=input("Ingrese la posición actual de la Torre ")
    return x
def obtenerPosicion(pos):
    fila= 8-int(pos[1])
    columna= ord(pos[0])-ord('a')
    posicion=(fila, columna)
    return posicion
def imprimirMatriz(matriz):
    print("  a b c d e f g h")
    for i in range(8):
        print(f"{8-i}",end=' ')  
        for j  in range(8):
            print(matriz[i,j], end=' ') 
        print("")
pos=validar()
estructura=obtenerPosicion(pos)
print(f"La posición de la Torre es: {estructura}")
matriz=np.full((8,8),fill_value='-')
matriz[estructura[0],:]='*'
matriz[:,estructura[1]]='*'
matriz[estructura[0], estructura[1]]='T'
imprimirMatriz(matriz)