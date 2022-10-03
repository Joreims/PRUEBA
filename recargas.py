class recargar:
def recarga(){
    def __init__(self,num,com, mon):
    self.Celular = num
    self.compañía = com
    self.Monto = mon

    def __str__(self):
return f"""Celular: {self.Celular}
Compañía: {self.compañía}
Monto: {self.Monto}
"""
}

class listarecarga:
    def __init__(self):
        self.recargaTIGO = []
        self.recargaCLARO = []
    def agregarRecargaTIGO(self,r)
        try:    
            self.recargaTIGO.append(r)
        except Exception as ex:
            print("Error al agregar: ", str(ex))
    def agregarRecargaCLARO(self,r)
        try:    
            self.recargaCLARO.append(r)
        except Exception as ex:
            print("Error al agregar: ", str(ex))




