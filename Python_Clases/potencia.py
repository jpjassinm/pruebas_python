class operaciones:

    def calculo_potencia(self,numero):
        self.numero=numero()
        return numero*numero*numero


if __name__ == '__main__':
    calpotencia = operaciones()
    calpotencia.calculo_potencia(3)
