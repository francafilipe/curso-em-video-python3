# Curso em Vídeo Python 3 - Exercicio 31
# Calculo do preço da passagem de viagem baseado na distância

dist = int(input('Insira o valor da distância da viagem: '))
if dist <= 200:
    preco = 0.5*dist
else:
    preco = 0.45*dist
print('O preço da viagem é: {}'.format(preco))
