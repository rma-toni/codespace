def main():
    lista = ["Toni","Genesis","Marco","Antonio"] #lista de una dimension

    for i in range(0,len(lista)):
        print(lista[i])
    print("--------")
    for item in lista:
        print(item)

    print("---MULTIDIMENSIONAL LISTS---")
    lista1 = [1,['a','r','i','o','u'],9.8,'hola',True] #lista de dos dimensiones
    print(lista1[1][3])

    #ENUMERATE use 
    print("---ENUMERATE USE---")
    lista2 = [["Toni",1],["Genesis",2],["Marco",3],["Antonio",4]]

    for i, item in enumerate(lista2):
        print(i)
        print(item)

    #SLICING
    print("---SLICING---") # listName[i:f:p] inicio, final, paso
    vocales = ['a','e','i','o','u']
    print(vocales[1:5:2])


    #CREAR ASIGNAR Y MODIFICAR
    lst1 = []        #lista vacia
    lst2 = list()    #lista vacia
    lst1.append(10)  #agrega un elemento al final
    lst1.insert(0,2) #inserta el seugundo elemento de la posicion que se encuentra primero
    #los operadores + y * generan nuevas listas, el * duplica la lista y el + las suma

    #COMPRESION
    #res1 = [x for x in lsta if x  >3] [Expresion <for> item for <iterable> if <condicion>]

    #Operador is in
    a = [1,2,3]
    b = [1,2,3]
    c = a
    print(a is b) #True //el operador is devuelve true si el objeto es el mismo, osea que este alojado en la misma direccion de memoria
    print(a is c) #True


    #RESUMEN DE METODOS
    print("---RESUMEN-METODOS---")
    listaFinal1 = [1,2,3]
    listaAux = [5,6]
    listaFinal1.append(4)
    listaFinal1.extend(listaAux)
    listaFinal1.insert(0,0)
    print(listaFinal1)
    listaFinal1.remove(0)
    del listaFinal1[len(listaFinal1)-1]
    print(listaFinal1)
    listaFinal1.sort() #ordena la lista
    listaFinal1.index(3) #retorna el indice de la primera ocurrencia de x
    lista.count(3) #retorna la cantidad de ocurrencias de x

if __name__ == "__main__":
    main()