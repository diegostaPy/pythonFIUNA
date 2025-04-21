limite = float(input("Ingrese el limite: "))
suma = 0
i = 1
while suma <= limite:
    if (suma + (2**i / i)) > limite:
        i -= 1
        break
    else:
        suma += (2**i / i)
        #print(f"El valor de suma es {suma} y de i es {i}")    
        i += 1
    

print(f"El valor de n es {i}")
print(f"La suma es {suma}")
