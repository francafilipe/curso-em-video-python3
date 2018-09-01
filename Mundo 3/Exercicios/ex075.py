# Curso em Vídeo Python 3 - Exercicio 75
# Análise de dados em uma Tupla

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))
num4 = int(input('Digite o quarto numero: '))
numeros = (num1, num2, num3, num4)
print('Foi digitados os valores: {}'.format(numeros))

cont9 = 0
print('Os numeros pares digitados foram: ', end='')
for pos, num in enumerate(numeros):
    if num % 2 == 0:
        print(num, end=' ')
    if num == 9:
        cont9 += 1
    if num == 3:
        posicao = pos

print('\nO valor 9 apareceu {} vezes.'. format(cont9))
print('O valor 3 apareceu na {}° posição'.format(posicao + 1))
