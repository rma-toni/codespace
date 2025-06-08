# Una empresa de comiones registra sus toneladas en listas paralelas denominadas
# numeros de comiones (int), destinos (string) y tonaeladas cargadas (flaot).
# Diseña en python los modulos y las acciones de llamadas que resuelvan lo siguiente.
# (no es necesario hacer el menu de opciones) pero igual

# 1-Agregar un numero de Camiom. validando que no se repita el numero de camion.
# 2-dado el numero de camion modificar el destino y la tonelada cargada.
# 3-listar y mostrar los datos de los camiones que tengan el mismo destino

    # {"camiones": 4, "destino": "Houston", "toneladas": 15.3},
    # {"camiones": 2, "destino": "Barcelona", "toneladas": 8.9},
    # {"camiones": 6, "destino": "Toronto", "toneladas": 27.4},
    # {"camiones": 3, "destino": "Berlin", "toneladas": 13.2}

numeroCamiones = []
destinos = []
toneladasCargadas = []

def agregarCamion():
    numCamion = int(input("Ingrese el numero de camion: "))
    while(numCamion in numeroCamiones):
        numCamion = int(input("El camion ya existe, ingrese uno nuevo: "))
    numeroCamiones.append(numCamion)
    destinos.append(input("Ingrese el destino: "))
    toneladasCargadas.append(float(input("Ingrese cuantas toneladas carga: ")))

def busquedaDestino():
    destinoBuscar = input("Ingrese el destino que desea buscar: ")
    for i, destino in enumerate(destinos):
        if(destino == destinoBuscar):
            print(f"Camion: {numeroCamiones[i]}, Destino: {destinos[i]}, Toneladas cargadas: {toneladasCargadas[i]}")


def mostrarListas():
    for i in range(len(numeroCamiones)):
        print(f"Camion: {numeroCamiones[i]}, Destino: {destinos[i]}, Toneladas cargadas: {toneladasCargadas[i]}")

def menu():
    while(True):
        print("1 - Agregar camion")
        print("2 - Buscar por destino")
        print("3 - Mostrar todo el listado")
        print("0 - Finalizar")
        selection = int(input("Ingrese una opcion (0 para salir): "))
        if(selection == 1):
            agregarCamion()
        elif(selection == 2):
            busquedaDestino()
        elif(selection == 3):
            mostrarListas()
        elif(selection == 0):
            break
    
menu()