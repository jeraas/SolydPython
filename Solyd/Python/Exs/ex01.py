# faça um formulario q pergunte o nome cpf endereco idade altura e telefone e imprima isso em um relatioro organizado

nome = str(input('Digite seu nome: ')).strip()
cpf = input('Digite seu cpf: ').strip()
endereco = input('Digite seu endereço: ').strip()
idade = int(input('Digite sua idade (numeral):'))
altura = input('Digite a sua altura: ').strip()
telefone = int(input('Digite seu telefone: '))

print('Seu nome: {}'.format(nome))
print('Seu cpf: {}'.format(cpf))
print('Seu endereço: {}'.format(endereco))
print('Sua idade: {}'.format(idade))
print('Sua altura: {}'.format(altura))
print('Seu telefone: {}'.format(telefone))