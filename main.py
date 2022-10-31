from docente import DocenteH
from estudiante import EstudianteH
from nota import NotaH
from fecha import FechaH

lista=[]

f=FechaH(27,10,2022)
n=NotaH(1,7,f)
e=EstudianteH(100,"Alex Verdugo","4° medio",n)
d=DocenteH(11,"JEBO","Programacion",e)
lista.append(d)

f=FechaH(27,10,2022)
n=NotaH(1,7,f)
e=EstudianteH(100,"Alex Verdugo","4° medio",n)
d=DocenteH(11,"Mariela","matematicas",e)
lista.append(d)

f=FechaH(27,10,2022)
n=NotaH(1,7,f)
e=EstudianteH(100,"Alex Verdugo","4° medio",n)
d=DocenteH(11,"Juan","Base de datos",e)
lista.append(d)

f=FechaH(27,10,2022)
n=NotaH(1,7,f)
e=EstudianteH(100,"Alex Verdugo","4° medio",n)
d=DocenteH(11,"Sebastian","Sistema Operativo",e)
lista.append(d)

f=FechaH(27,10,2022)
n=NotaH(1,7,f)
e=EstudianteH(100,"Alex Verdugo","4° medio",n)
d=DocenteH(11,"Carlos","Desarrollo Agil",e)
lista.append(d)

def salir():
    print("Saliendo del programa...")
    exit()

def main():
    while True:
        print("|****************************|")
        print("|**|      Bienvenidos     |**|")
        print("|**|         Menu         |**|")
        print("|****************************|")
        print("")
        print("Seleccione una de las siguientes opciones:")
        print("1.- Agregar un Docente nuevo: ")
        print("2.- Agregar un Estudiante")
        print("3.- Modificar Nota Estudiante")
        print("4.- Eliminar Nota Estudiante")
        print("5.- Mostrar Promedio Estudiante")
        print("6.- Salir")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            print("opcion 1")
        elif opcion == 2:
            print("opcion 2")
        elif opcion == 3:
            print("opcion 3")
        elif opcion == 4:
            print("opcion 4")
        elif opcion == 5:
            print("opcion 5")
        elif opcion == 6:
            salir()
        else:
            print("Digite una opcion valida!")

if __name__ == '__main__':
    main();
 