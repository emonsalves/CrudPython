from os import system
from docente import DocenteH
from estudiante import EstudianteH
from nota import NotaH
from fecha import FechaH

lista = []

f = FechaH(27, 10, 2022)
n = NotaH(1, 7, f)
e = EstudianteH(100, "Alex Verdugo", "4° medio", n)
d = DocenteH(11, "JEBO", "Programacion", e)
lista.append(d)

f = FechaH(27, 10, 2022)
n = NotaH(2, 7, f)
e = EstudianteH(100, "Alex Verdugo", "4° medio", n)
d = DocenteH(12, "Mariela", "matematicas", e)
lista.append(d)

f = FechaH(27, 10, 2022)
n = NotaH(3, 7, f)
e = EstudianteH(100, "Alex Verdugo", "4° medio", n)
d = DocenteH(13, "Juan", "Base de datos", e)
lista.append(d)

f = FechaH(27, 10, 2022)
n = NotaH(4, 7, f)
e = EstudianteH(100, "Alex Verdugo", "4° medio", n)
d = DocenteH(14, "Sebastian", "Sistema Operativo", e)
lista.append(d)

f = FechaH(27, 10, 2022)
n = NotaH(5, 7, f)
e = EstudianteH(100, "Alex Verdugo", "4° medio", n)
d = DocenteH(15, "Carlos", "Desarrollo Agil", e)
lista.append(d)


def salir():
    print("Saliendo del programa...")
    exit()


def main():
    while True:
        print("|*************************************|")
        print("|*************************************|")
        print("|**|           Bienvenidos         |**|")
        print("|**|               Menu            |**|")
        print("|*************************************|")
        print("|*************************************|")
        print("")
        print("")
        print("Seleccione una de las siguientes opciones:")
        print("1.- Agregar un Docente nuevo: ")
        print("2.- Agregar un Estudiante")
        print("3.- Modificar Nota Estudiante")
        print("4.- Eliminar Nota Estudiante")
        print("5.- Mostrar Promedio Estudiante")
        print("6.- Salir")

        try:
            opcion = int(input("Opcion: "))

        except ValueError:
            system("cls")
            print("|*************************************|")
            print("|**|Error ingrese una opcion valida|**|")
            print("|**|                               |**|")
            print("|*************************************|")
            print("")
            print("")
            opcion = 0

        if opcion == 1:
            idIngresada = int(input("Ingrese el ID: "))
            d.agregarDocente(idIngresada, lista)

        elif opcion == 2:
            idIngresad = int(input("Ingrese el ID: "))
            e.agregarEstudiante(idIngresad, lista)

        elif opcion == 3:
            print("opcion 3 ---------------------------------------------")
        elif opcion == 4:
            print("opcion 4 ---------------------------------------------")
        elif opcion == 5:
            print("opcion 5 ---------------------------------------------")
        elif opcion == 6:
            salir()

            
main()
