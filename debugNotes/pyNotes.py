def sumaPares():
    #Dada una lista de enteros, devolvé la suma de todos los números pares.
    #numeros = [10, 3, 4, 7, 2, 8]
    #Resultado esperado: 24 (10+4+2+8)
    numeros = [10, 3, 4, 7, 2, 8]
    acc = 0
    for num in  numeros:
        if(num % 2 == 0):
            acc += num
    return acc

def eliminarDuplicados():
    # Dada una lista, devolvé una nueva lista sin elementos duplicados, pero manteniendo el orden.
    # entrada = [1, 2, 3, 2, 1, 4]
    # # Resultado esperado: [1, 2, 3, 4]
    entrada = [1, 2, 3, 2, 1, 4]
    finalList = []
    for item in entrada:
        if(not item in finalList):
            finalList.append(item)
    return finalList

def rotarIzquierda():
    # Rotar una lista una posición hacia la izquierda.
    entrada = [1, 2, 3, 4]
    # Resultado esperado: [2, 3, 4, 1]
    listaRotada = []
    for i in range(len(entrada)):
        if (i < (len(entrada)-1)):
            listaRotada.append(entrada[i+1])
        else:
            listaRotada.append(entrada[0])
    return listaRotada

def sumaMatriz():
    #Dada una matriz (lista de listas) de números, devolver la suma total de todos sus elementos.
    matriz = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    # Resultado esperado: 21
    acc = 0
    for fila in matriz:
        for item in fila:
            acc+=item
    return acc

def trasponerMatriz(): #A Completar
    #Dada una matriz, devolvé su transpuesta.
    matriz = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    matrizTraspuesta = []
    # Resultado esperado:
    # [
    #   [1, 4],
    #   [2, 5],
    #   [3, 6]
    # ]
    
    columnasT = len(matriz)
    filasT = len(matriz[0])

    for i in range[filasT]:
        fila = [matriz[0+i][i]]
        matrizTraspuesta.append[0]

def contarLetras():
    #Dado un string, devolvé un diccionario con la cantidad de veces que aparece cada letra (ignorando espacios y usando minúsculas).
    texto = "Hola Mundo"
    # Resultado esperado:
    # {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}
    letrasAcc = {}
    for char in texto:
        if char != ' ':
            if char.lower() in letrasAcc:
                letrasAcc[char.lower()] = letrasAcc[char.lower()]+1
            else:
                letrasAcc[char.lower()] = 1
    return letrasAcc

def main():
    print(contarLetras())
    
if __name__ == "__main__":
    main()