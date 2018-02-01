valor = int(input("Cuants nombres introduira: "))
primer=0
numero=0

if valor < 1:
    print("Boig")
else:
    primer= int(input("Escriu un nombre: "))
    for i in range(valor - 1):
        numero = int(input("Escriu un nombre mes gran que el: " ,numero))
        if numero <= primer:
            print(numero "no es mes gran",primer)
        primer = numero
