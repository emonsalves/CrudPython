from fecha import FechaH


class NotaH():
    def __init__(self, idNota, calificacion, fechaN):
        self.idNota = idNota
        self.calificacion = calificacion
        self.fechaN = fechaN

    def mostrarNota(self):
        return "\nId Nota      : "+str(self.idNota) +\
            "\nCalificacion : "+str(self.calificacion)
