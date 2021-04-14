
from random import randint


# Este es una funcion para imprimir numeros a la azar

def numero_loteria():

    for i in range(100000):
        numero = randint (0,9999)
        serial = randint(0,999)
        resultado = (i, "El numero de la suerte es ", numero, " con el serial ", serial)

        print(str(resultado))
        print("Todo esta bien")



numero_loteria()



