from nota import NotaH


class EstudianteH():
    def __init__(self, idEstudiante, nombre, curso, nota):
        self.idEstudiante = idEstudiante
        self.nombre = nombre
        self.curso = curso
        self.nota = nota

    def mostrarEstudiante(self):
        return "\nId Estudiante  : "+str(self.idEstudiante) +\
            "\nNombre         : "+self.nombre +\
            "\nCurso          : "+self.curso

    def buscarEstudiante(self, idBuscar, lista):
        for q in lista:
            if idBuscar == self.idEstudiante:
                return q
        return None  # None es un objeto nulo o null

    def agregarEstudiante(self, idNuevo, lista):
        if self.buscarEstudiante(idNuevo, lista) == None:
            nombre = input("Nombre: ")
            curso = input("Curso: ")
            d = EstudianteH(idNuevo, nombre, curso, None)
            lista.append(d)

        else:
            print("Id Ocupado por Estudiante")
        return lista
