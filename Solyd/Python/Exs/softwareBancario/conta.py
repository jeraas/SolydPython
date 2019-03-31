from cliente import Cliente

class Conta:
    def __init__(self, saldo, limite, nome, cpf, idade):
        Cliente.__init__(self, nome, cpf, idade)
        self.saldo = saldo
        self.limite = limite
    def sacar(self, quantidade):
        if quantidade <= 0:
            print('Erro.')
        else:
            if self.saldo - quantidade < self.limite:
                print('Erro! O seu limite de saldo não permite que você faça uma retirada no valor de R${}.'.format(quantidade))
                print(' ')
            else:
                self.saldo = self.saldo - quantidade
                print('Retirada feita com sucesso!')
                print('Seu saldo atual agora é: R${}'.format(self.saldo))
                print(' ')
    def depositar(self, quantidade):
        if quantidade > 0:
            self.saldo = self.saldo + quantidade
            print('Depósito feito com sucesso!')
            print('Seu saldo atual agora é R${}'.format(self.saldo))
            print(' ')
        else:
            print('Erro no depósito.')
            print(' ')
    def information(self):
        print(' -- Informações Pessoais -- ')
        print('Nome:', self.nome)
        print('CPF:', self.cpf)
        print('Idade:', self.idade)
        print('\n')
        print(' -- Informações Bancarias -- ')
        print('Seu saldo:', self.saldo)
        print('Seu limite bancário:', self.limite)
        print(' ')
