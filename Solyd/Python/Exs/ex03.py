from random import randint

convidados = []

for convidado in range(1, randint(2, (5 + 1))):
    nome = str(input('Digite o nome do convidado: '))
    convidados.append(nome)
print('\n')
print('\n')
print('Convidados: ')
for nome in convidados:
    print(nome)