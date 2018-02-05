num=int(input("Escribe un numero: "))
yes=0

while(num!=0):

    if not(num%2):
        print("No es primo")
        break
    if not(num%3):
        print("No es primo")
        break
    if not(num%5):
        print("No es primo")
        break 
    if not(num%7):
        print("No es primo")
        break
    if not(num%11):
        print("No es primo")
        break
    print("Probablemente es primo")
    break
