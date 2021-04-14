
class Coordenada:

    #inicializamos el metodo constructor
    def __ini__(self, x, y):
        #inicializamos las variables
        self.x = x
        self.y = y


    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

#Inicializamos el programa siempre con el siguiente parametro:
if __name__ == '__main__':
    coord_1 = Coordenada(2, 30)
    coord_2 = Coordenada(4, 8)

    #print(coord_1.distancia(coord_2))
    print(isinstance(coord_2, Coordenada)) # revisamos que coor2, sea una instancia de Coordenada