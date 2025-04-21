N=5
i=1
while(i<=100):
    i=i+1 # contador
    x=int(input())    
    if(x>=90 and x<=100):
        nota=5
    elif(x>=80 and x<90):
        nota=4
    elif(x>=70 and x<80):
        nota=3
    elif(x>=60 and x<70):
        nota=2
    else:
        nota=1    
    print("La nota es:",nota)