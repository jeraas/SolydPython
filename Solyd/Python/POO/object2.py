from object1 import Veiculo

class Carro(Veiculo):
    def __init__(self, cor, marca, tanque, capLitros):
        Veiculo.__init__(self, cor, 4, marca, tanque, capLitros)
