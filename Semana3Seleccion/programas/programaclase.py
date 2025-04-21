#este programa
p=float(input())
if p<0:
    print("EL numero es negativo")
if p>100:
    print("EL numero es mayor que 100")
if(p>=0 and p<=100): 
    if(p>=90 and p<=100):
        print("La nota es 5")
        print("Excelente")
    elif p>=80:   #p>80 and p<90
        print("La nota es 4")
    elif p>=70:  
        print("La nota es 3")
    elif p>=60:  
        print("La nota es 2")
    else:
        print("La nota es 1")
    



