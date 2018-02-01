num=int(input("Escribe un numero: "))
num1=int(input("Escribe otro: "))
num2=0

while (num>0 and num1>0):
    num=num1
    num=int(input("Escribe otro: "))
    num2=num+num1
    
print("No puede ser negativo")
print("Suma de los valores introducidos") str(num2)
