def main():
    #---SINTAXIS---
    dic = {}
    dic = dict()
    dic = {"clave1" : "valor1", "clave2" : 3}

    #---METODOS---
    dict = {"hola" : 23}
    dict.clear() #elimina todos los elemetnos
    dict.copy() #devuelve una copia
    dict.get("hola",default=None)
    dict.items()
    dict.keys()
    dict.pop("hola",default = None)
    dic.popitem() #elimina una clave al azar, error si esta vacio
    dict.setdefault("hola", default=None) #igual que get pero si no existe la crea con el valor por default
    dict.update(dict2) #añade el dict2 a dict1 sobrescribe si ya existe clave
    dict.values() #devuelve la lista de los valores del diccionario

if __name__ == "__main__":
    main()