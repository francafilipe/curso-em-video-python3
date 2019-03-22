# Curso em Vídeo Python 3 - Exericio 100
# Funções para sortear e somar

from random import randint
from time import sleep

def sortear(n):
    numeros = list()
    print('Sorteando valores...')
    sleep(1.5)
    for i in range(0, n):
        num = randint(0, 10)
        numeros.append(num)
    return numeros


def soma(numeros):
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    return soma


n = int(input('Quantos numeros a serem sorteados? '))
nums = sortear(n)
print(nums)
print('A soma dos números pares sorteados é: {}'.format(soma(nums)))
