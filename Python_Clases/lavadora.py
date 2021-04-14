
class Lavadora:

    def __init__(self):
        pass


    def lavar(self, temperatura = 'caliente'):
        self._llenar_tanque(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugando()


    def _llenar_tanque(self,temperatura):
        print(f'llenando el taque con agua {temperatura}')


    def _anadir_jabon(self):
        print('añadiendo jabon')


    def _lavar(self):
        print('esta lavando la ropa')
        

    def _centrifugando(self):
        print('centrifugando la ropa')


if __name__ == '__main__':

    #Creamos la instacia de la clase
    play = Lavadora()
    play.lavar()
        
        

        


