#realizar un modulo denominado elimnar_palabras_cortas(cad) que, el parametro cad, recibe una frase
#compuesta separada por espacios, la funcion debe elimnar las palabras que tengan menos de cuatro caracteres.
#se debe retornar la frase con los cambios

def eliminar_palabras_cortas(cad):
    list_cad = cad.split(" ")
    list_final = []
    for palabra in list_cad:
        if(len(palabra)>=4):
            list_final.append(palabra)
    print(list_final)
    cad_final = ' '.join(list_final)
    return(cad_final)

def main():
    cadena = "Hola que tal esto es una frase larga"
    print(eliminar_palabras_cortas(cadena))

if __name__ == "__main__":
    main()