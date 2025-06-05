#1. Mediante un menú de opciones realizar el siguiente programa modular para gestionar el listado de notas de un
#examen para los estudiantes de una institución educativa:
#1. Registrar estudiantes: para cada uno se debe solicitar DNI, nombre y nota. Validar que la nota se
#encuentre entre 0 y 10. El proceso finaliza cuando se ingresa un DNI igual a cero.
#2. Mostrar el listado de estudiantes con sus respectivas notas.
#3. Buscar a un estudiante por su DNI y mostrar su nombre y nota.
#4. Modificar los datos de un estudiante buscando por DNI (el DNI no se puede modificar).
#5. Eliminar a un estudiante por su DNI. Emitir un mensaje de confirmación.
#6. Mostrar los estudiantes que obtuvieron nota mayor o igual a una dada y el promedio correspondiente.
import os

students = {}

def regEstudiante():
    while(True):
        dni = int(input("Ingrese el DNI del estudiante (0 para dejar de ingresar estudiantes): "))
        if(dni == 0):
            return
        nombre = input("Ingrese el nombre del estudiante: ")
        nota = int(input("Ingrese la nota del estudiante: "))
        while(nota <= 0 and nota >= 10):
            nota = int(input("ingrese una nota valida(entre 0 y 10): "))
        students[dni] = [nombre, nota]

def mostrarListado():
    print(students)

def buscarEstudiante():
    dni = int(input("Ingrese el DNI del estudiante que desea buscar: "))
    print(students.get(dni))

def modificarEstudiante():
    dni = int(input("Ingrese el DNI del estudiante que desea modificar: "))
    if(students.get(dni) == None):
        print("El estudiante no existe!")
        return
    nombre = input("Ingrese el nuevo nombre del estudiante: ")
    nota = int(input("Ingrese la nueva nota del estudiante: "))
    students[dni] = [nombre, nota]

def eliminarEstudiante():
    dni = int(input("Ingrese el DNI del estudiante que desea eliminar: "))
    if(students.get(dni) == None):
        print("El estudiante no existe!")
        return
    students.pop(dni)
    print(f"Estudiante {dni} eliminado con exito")

def notaMayorIgual(nota):
    acc = 0
    counter = 0
    for student in students:
        aux = students[student]
        if(aux[1] >= nota):
            acc += aux[1]
            counter += 1
            print(students[student]) 
    if(counter == 0):
        print("No se encontraron estudiantes")
        return
    print(f"La nota promedio de estos estudiantes es: {acc/counter}")

def menu():
    while(True):
        #os.system("cls")
        print(f"Bienvenido".center(20))
        print("1 - Registrar Estudiantes")
        print("2 - Mostrar Listado")
        print("3 - Buscar por estudiante")
        print("4 - Modificar estudiante")
        print("5 - Eliminar estudiante")
        print("6 - Mostrar estudiantes por nota")
        print("0 - Salir del programa")
        option = int(input("Ingrese la opcion deseada: "))

        if(option == 1):
            os.system("cls")
            regEstudiante()
        elif(option == 2):
            os.system("cls")            
            mostrarListado()
        elif(option == 3):
            os.system("cls")
            buscarEstudiante()
        elif(option == 4):
            os.system("cls")
            modificarEstudiante()
        elif(option == 5):
            os.system("cls")
            eliminarEstudiante()
        elif(option == 6):
            os.system("cls")
            nota = int(input("Ingrese la nota: "))
            notaMayorIgual(nota)
        elif(option == 0):
            break
        elif(True):
            os.system("cls")
            print("Opcion invalida, vuelva a insartar una opcion correcta")


menu()