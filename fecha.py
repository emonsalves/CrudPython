class FechaH():
    def __init__(self,dd,mm,aa):
        self.dd=dd
        self.mm=mm
        self.aa=aa
    
    def mostrarFecha(self):
        return  str(self.dd)+"/"+str(self.mm)+"/"+str(self.aa)