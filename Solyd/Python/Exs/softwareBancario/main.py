from cliente import Cliente
from conta import Conta

def createClient():
    print(' -- Criação de Cliente -- ')
    nome = str(input('Nome: '))
    cpf = str(input('CPF: '))
    idade = str(input('Idade: '))
    newUser = Cliente(nome, cpf, idade)
    return newUser

def createAccount(client, saldo, limite):
    if client:
        newAccount = Conta(saldo, limite, client.nome, client.cpf, client.idade)
        return newAccount


newUser = createClient()
newAccount = createAccount(newUser, 1000, -500)

print('\n')

def menu():
    print('Bem vindo ao menu.')
    print('Escolha uma das ações a seguir: ')
    print('[1] Sacar')
    print('[2] Depositar')
    print('[3] Ver informações')
    print('[0] Sair')
    while True:
        op = int(input(' '))
        if op == 1 or op == 2 or op == 3 or op == 0:
            break
        else:
            print('Opção inválida. Tente novamente.')
    return op

again = 'y'
while again == 'y':
    opcao = menu()
    if opcao == 1:
        quantidade = float(input('Digite a quantidade: '))
        print(' ')
        newAccount.sacar(quantidade)
    elif opcao == 2:
        quantidade = float(input('Digite a quantidade: '))
        print(' ')
        newAccount.depositar(quantidade)
    elif opcao == 3:
        print(' ')
        newAccount.information()
    elif opcao == 0:
        again = 'n'
        break
    again = str(input('Deseja fazer alguma outra ação? [y/n]'))
    while True:
        if again[0].lower() == 'y':
            again = 'y'
            break
        elif again[0].lower() == 'n':
            again = 'n'
            break
        else:
            print('Opção inválida. Tente novamente.')
            again = str(input('Deseja fazer alguma outra ação? [y/n]'))


