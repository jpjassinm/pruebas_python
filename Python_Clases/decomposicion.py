
class Automovil:
    
    def __init__(self, modelo, marca, color):
        #inicializamos las variables
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = "en reposo"
        self._motor = Motor(Cilindro=4)

    

class Motor:

    def __init__(self, Cilindro, tipo="Gasolina"):
        #inicializamos la variable
        self.Cilindro = Cilindro
        self.tipo = tipo
        self._temperatura = 0

    
    def inyecta_gasolina(self, cantidad):
