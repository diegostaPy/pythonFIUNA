dia=int(input())
mes=int(input())
anho=int(input())

esBisiesto=(anho % 4 == 0 and not(anho % 100 == 0)) or (anho % 400 == 0)
if(dia==31 and mes==12):
    dia=1
    mes=1
    anho=anho+1
elif ((mes==4 or mes==6 or mes== 9 or mes==11) and dia==30):
    dia=1
    mes=mes+1
elif((mes==1 or mes==3 or mes== 5 or mes==7 or mes==8 or mes==10) and dia==31):
    dia=1
    mes=mes+1
elif(mes==2 and esBisiesto and dia==29):
    dia=1
    mes=3
elif(mes==2 and not(esBisiesto) and dia==28):
    dia=1
    mes=3
else:
    dia=dia+1
print(dia,mes,anho)
    

    



#if (anho % 4 == 0 and anho % 100 != 0) or (anho % 400 == 0):