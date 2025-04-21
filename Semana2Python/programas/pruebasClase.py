"""
Este programa muestra los tipos de datos basicos de python

"""
a=5
print(a)
print(a**2)
print(a+1)
print(type(a))
b=5.
print(type(b))
c="Diego"
print(c)
print(type(c))
print(c*5)
print(c+str(1))
# idendentificadores no validos
#-a=1
#2a=1
#$a=1


a=True
print(a)
print(type(a))
b=5>2
print(b)
c=(3+2.)==5
print(c)

x=10e10
print(x)
y=5+5j
print(type(y))
z=1+6j
print(y+z)


b=10
c=11
d=5.1
print(b%2)
print(c%2)
print(int(d)%2)
print(b%2==0)

print(b%c)

print(type(5//2))
print(5//2)


#entrada 

x=float(input("Cargue un numero entero: "))
#x=int(input()) para el vpl se recomienda
print("El numero ingresado al cuadrado es "+str(x**2))

print("El numero ingresado al cuadrado es ",x**2,sep="-",end="*\n")
print(f"El numero ingresado al cuadrado es {x**2:.3f}")

print("El numero ingresado %f al cuadrado es %f"% (x,x**2))
