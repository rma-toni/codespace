def main():
    print("---ESTRUCTURA-DE-UNA-CADENA---")
    cadena1 = "Hola a todos"
    print(cadena1)
    cadena2 = "como estan?"
    cadena3 = cadena1 + " " + cadena2
    len3 = len(cadena3)
    print(cadena3)
    #RECODAR QUE LOS STINGS SON INMUTABES, no permite la asignacion directa s[5] = 'A'
    print(f"La cantidad de caracteres que hay en cadena3 es de = {len3}")
    #RECORDAR QUE EN PITON EL + SOLO SE USA (EN STRINGS) PARA CONCATENAR STRINGS Y SOLO STRINGS

    #EL SLICING SE HACE IGUAL QUE EN LAS LISTAS INICIO FINAL STEP

    print("\n---METODO-FORMAT---")
    txt = 'Soy {nombre}, tengo {edad} años'
    print(txt.format(nombre = 'Toni', edad = '16'))

    print("\n---METODOS---")
    s = 'hOlA mUNdo cRuEL '
    s.find('m') #primera coincidencia
    s.rfind('u') #ultima ocurrencia
    s.find('el') #cadena desde atras
    s.count(' ') #cuantes veces aparec
    s.capitalize()
    s.lower()
    s.upper()
    s.swapcase()
    s.title()
    s.center(30,'.')
    s.ljust(30,'.')
    s.rjust(30,'.')
    s.zfill(30)
    t = s.replace('hOlA',' Chau')
    t.lstrip()#elimina espacio a la izquierda
    t.rstrip()
    t.strip()

    print("\n---SEPARAR-UNIR---")
    a = '192.168.1'.split('.') #devuelve una lista, el argumento es el separador
    #".".join une los elementos en un string, en este caso unidos por un punto

    print("\n--OTROS-METODOS-BOOLEAN---")
    cad = "2"
    cad.isdigit()
    cad.isalnum()
    cad.isalpha()
    cad.islower()
    cad.istitle()
    cad.isspace()
    cad.startswith("sub") 

if __name__ == "__main__":
    main()