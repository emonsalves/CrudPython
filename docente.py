from estudiante import EstudianteH

class DocenteH():
    def __init__(self,idDocente,nombre,asignatura,estudiante):
        self.idDocente=idDocente
        self.nombre=nombre
        self.asignatura=asignatura
        self.estudiante=estudiante

    def mostrarDocente(self):
        "\nId Docente   : "+str(self.idDocente)+\
        "\nNombre       : "+self.nombre+\
        "\nAsignatura   : "+self.asignatura