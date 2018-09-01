# Curso em Vídeo Python 3 - Exercicio 75
# Análise de dados em uma Tupla

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))
num4 = int(input('Digite o quarto numero: '))
numeros = (num1, num2, num3, num4)
print('Foram digitados os valores: {}'.format(numeros))

print('Os numeros pares digitados foram: ', end='')
for pos, num in enumerate(numeros):
    if num % 2 == 0:
        print(num, end=' ')

print('\nO valor 9 apareceu {} vezes.'. format(numeros.count(9)))
if 3 in numeros:
    print('O valor 3 apareceu na {}° posição'.format(numeros.index(3)))
else:
    print('O valor 3 não foi digitado.')
