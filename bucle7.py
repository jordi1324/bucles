lim1=int(input("Escriba un limite1: "))
lim2=int(input("Escriba un limite2: "))
num1=0
x=0

while (lim1>lim2 ):
    num1=int(input("Escribe un numero entre los dos limites:  "))
    x=x+num1
    if (num1<lim2 or num1>lim1):
        print("Has escrito tantos numeros entre los limites", x)
        break
