import math

w=1
v='a'
counter = 0
while w != 0:
    v = input("Ingrese un caracter: ")
    w = int(input("Ingrese un valor entero: "))
    if(v == 'A'):
        if(w > 0):
            print("w es positivo")
        else:
            print("w es negativo")
    elif(v == 'B'):
        print(math.sqrt(1/w))
    elif(v == 'C'):
        print("Ok")
    else:
        counter+=1
print(f"Valores de v que no fueron A, B o C = {counter}")
