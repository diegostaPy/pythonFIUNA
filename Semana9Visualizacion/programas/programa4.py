
while(True):
    try:
        A=int(input())
        break
    except ValueError:
        print("debe cargar un numero entero")
    
print(A)