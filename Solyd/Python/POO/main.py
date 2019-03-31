from object1 import Veiculo
from object2 import Carro

carroFord = Carro('Preto', 'Ford', 40, 100)

print('Cor:', carroFord.cor)
print('Marca:', carroFord.marca)
print('Rodas: ', carroFord.rodas)
print('Tanque: ', carroFord.tanque)
print('Capacidade de litros: ', carroFord.capacidade)


print('\n')
carroFord.abastecer(999)

print('Tanque: ', carroFord.tanque)
print('Capacidade de litros: ', carroFord.capacidade)