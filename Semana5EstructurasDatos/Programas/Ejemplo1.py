'''
anho = int(input("Ingrese anho: "))
if anho < 1900 or anho > 2100: 
    print("El anho debe estar entre 1900 y 2100")
else:
    if anho%4==0 and (anho%100!=0 or anho%400==0):
        print(f"El anho {anho} es bisiesto")
    else:
        print(f"El anho {anho} NO es bisiesto")

anho = 0
while anho < 1900 or anho > 2100:
    anho = int(input("Ingrese anho: "))

if anho%4==0 and (anho%100!=0 or anho%400==0):
    print(f"El anho {anho} es bisiesto")
else:
    print(f"El anho {anho} NO es bisiesto")
    '''
ban = True
while ban:
    anho = int(input("Ingrese anho: "))
    if anho >= 1900 and anho <= 2100:
        ban = False

if anho%4==0 and (anho%100!=0 or anho%400==0):
    print(f"El anho {anho} es bisiesto")
else:
    print(f"El anho {anho} NO es bisiesto")