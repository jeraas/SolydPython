def high(object):
    maior = 0
    for item in object:
        if int(item) > maior:
            maior = item
    return maior

def low(object):
    menor = object[-1]
    for item in object:
        if int(item) < menor:
            menor = item
    return menor

objetos = []

for x in range(1, 6):
    objeto = int(input('Insira um valor numérico: '))
    objetos.append(objeto)

maior = high(objetos)
menor = low(objetos)

print('O maior valor da lista é: {}'.format(maior))
print('O menor valor da lista é: {}'.format(menor))