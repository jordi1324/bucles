num=int(input("Escriu un nombre: "))
num1=0
i=0
x=0
while (i<num):
    x=num+x
    num1=int(input("Escriu un positiu:"))
    if (num>i):
        x=num+num1
        i=i+1
        print(x)
        break
    
    
