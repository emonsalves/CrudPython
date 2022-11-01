from estudiante import EstudianteH


class DocenteH():
    def __init__(self, idDocente, nombre, asignatura, estudiante):
        self.idDocente = idDocente
        self.nombre = nombre
        self.asignatura = asignatura
        self.estudiante = estudiante

    def mostrarDocente(self):
        return "\nId Docente   : "+str(self.idDocente) +\
            "\nNombre       : "+self.nombre +\
            "\nAsignatura   : "+self.asignatura

    def buscarDocente(self, idBuscar, lista):
        for q in lista:
            if idBuscar == q.idDocente:
                return q
        return None  # None es un objeto nulo o null

    def agregarDocente(self, idNuevo, lista):
        if self.buscarDocente(idNuevo, lista) == None:
            nombre = input("Nombre: ")
            asignatura = input("Asignatura: ")
            d = DocenteH(idNuevo, nombre, asignatura, None)
            lista.append(d)
        else:
            print("Id Ocupado por Docente")
        return lista
