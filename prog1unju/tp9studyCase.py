# Analice, diseñe y codifique los siguientes enunciados en Python
# 1. Una institución bancaria tiene una aplicación que recibe una lista con los movimientos de las cuentas bancarias
# de sus clientes mediante un servicio externo. Para cada cuenta se recibe el número de cuenta, nombre y
# apellido del cliente, importe, fecha del movimiento y el tipo de movimiento (E=Extracción, D=Depósito). El
# formato de cada cuenta está dado por una cadena de caracteres donde cada atributo de una cuenta se
# encuentra separado por comas.
# Por ejemplo:
# 27200123456,MARIA FERNANDEZ,0000500000,30-05-2021,E
# 27200321654,CARLOS TORRES,0000400045,31-05-2021,D
# 27200987125,LAURA AQUINO,0000230000,30-05-2021,D
# 27200852369,MARTIN ESTRADA,0000700000,25-05-2021,E
# 27200123456,MARIA FERNANDEZ,0000250099,31-05-2021,E
# 27200795169,FLORENCIA ROBLES,0000350080,20-05-2021,D
# Tenga en cuenta que:
# - Los 2 últimos dígitos del importe corresponden a los centavos, o sea que el valor 0000500000 es
# equivalente a 5000 pesos.
# - La fecha solo tiene carácter informativo por lo que debe guardarse como un string.
# Se solicita lo siguiente:
# 1. Procesar la lista recibida y guardar los datos recibidos en una lista.
# 2. Mostrar la lista con las cuentas obtenidas.
# 3. Mostrar los movimientos correspondientes a depósitos y el total acumulado.
# 4. Mostrar los movimientos de una cuenta.
# Nota: utilice los datos del ejemplo para validar el programa

# Voy a hacer modificaciones propias al ejercicio

import os

def mostrarDepositos(data):
    print(f" DEPOSITOS ".center(68,"-"))
    for item in data:
        if(item[len(item)-1] == 'D'):
            print(item)

def mostrarExtracciones(data):
    print(f" EXTRACCIONES ".center(68,"-"))
    for item in data:
        if(item[len(item)-1] == 'E'):
            print(item)

def stringToInt():
    print("")
     
def main():
    os.system("cls")

    print(f" BIENVENIDO ".center(68,"-"))

    print(f" CUENTAS OBTENIDAS ".center(68,"-"))
    #print("\n")
    debugData = ["27200123456,MARIA FERNANDEZ,0000500000,30-05-2021,E","27200321654,CARLOS TORRES,0000400045,31-05-2021,D","27200987125,LAURA AQUINO,0000230000,30-05-2021,D","27200852369,MARTIN ESTRADA,0000700000,25-05-2021,E","27200123456,MARIA FERNANDEZ,0000250099,31-05-2021,E","27200795169,FLORENCIA ROBLES,0000350080,20-05-2021,D"]
    processedData = []
    for i, item in enumerate(debugData):
        processedData.append(item.split(","))
    for item in processedData:
        print(item)
    mostrarDepositos(processedData)
    mostrarExtracciones(processedData)

    
if __name__ == "__main__":
    main()
    