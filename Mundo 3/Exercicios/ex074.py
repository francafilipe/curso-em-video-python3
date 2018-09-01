# Curso em Vídeo Python 3 - Exercicio 74
# Maior e menor valor em Tuplas

from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os valores sorteados foram: ')
for i in numeros:
    print(i, end=' ')

print('\nO maior valor sorteado foi {}'.format(max(numeros)))
print('O menor valor sorteado foi {}'.format(min(numeros)))

"""
for pos, num in enumerate(numeros):
    print(num, end=' ')
    if pos == 0:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print('\nO maior valor sorteado foi {}'.format(maior))
print('O menor valor sorteado foi {}'.format(menor))
"""

