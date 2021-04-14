class Vacaciones:

    def __init__(self):
        pass

    def viaje(self):
        self._maleta()
        self._taxi()
        self._areopuerto()
        self-_subir_avion()

    
    def _maleta(self):
        print('Se empaca las maletas para el paseo')

    def _taxi(self):
        print('Se para un taxi para que nos lleve al areaopuerto')

    def _areopuerto(self):
        print('llegamos al areopuerto y esperamos el avion')

    def _subir_avion(self):
        print('mostramos el tiquete y subimos al avión')

    
    if __name__ == '__main__':
        
        descanso = Vacaciones() 
        descanso.viaje()



