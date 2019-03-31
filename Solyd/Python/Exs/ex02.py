idade = int(input('Sua idade: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

idadeN = 18
pesoN = 60.00
alturaN = 1.70

if idade > idadeN and peso >= pesoN and altura >= alturaN:
    print('Parabéns, você entrou no exército.')
else:
    print('Você não cumpre todos requisistos para entrar no exército.')