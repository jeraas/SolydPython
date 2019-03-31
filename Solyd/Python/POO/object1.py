class Veiculo:
    def __init__(self, cor, rodas, marca, tanque, capLitros):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque
        self.capacidade = capLitros
    def abastecer(self, litros):
        if self.tanque + litros > self.capacidade:
            self.tanque = self.capacidade
        else:
            self.tanque += litros
