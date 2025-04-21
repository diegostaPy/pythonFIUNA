def generarCadMayusculas(cadena):
    res = ''
    for l in cadena:
        if l>='a' and l<='z':
            res += chr(ord(l)-ord('a')+ord('A'))
        else:
            res += l
    return res

cad = 'Hola mundo'
print(generarCadMayusculas(cad))