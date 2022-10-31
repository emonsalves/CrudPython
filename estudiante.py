from nota import NotaH

class EstudianteH():
    def __init__(self,idEstudiante,nombre,curso,nota):
        self.idEstudiante=idEstudiante
        self.nombre=nombre
        self.curso=curso
        self.nota=nota
    
    def mostrarEstudiante(self):
        return  "\nId Estudiante  : "+str(self.idEstudiante)+\
                "\nNombre         : "+self.nombre+\
                "\nCurso          : "+self.curso
