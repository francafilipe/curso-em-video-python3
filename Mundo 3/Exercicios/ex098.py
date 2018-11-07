# Curso em Vídeo Python 3 - Exercicio 98
# Função de Contador

from time import sleep


def um_dez():
    for i in range(0, 11):
        if i != 10:
            print(i, end=' ')
            sleep(1)
        else:
            print(i)


def dez_zero():
    for i in range(10, -1, -2):
        if i != 0:
            print(i, end=' ')
            sleep(1)
        else:
            print(i)


def cont(i, f, p):
    if p == 0:
        p = 1
    if f > i:
        for j in range(i, f+1, p):
            print(j, end=' ')
            sleep(1)
    else:
        for j in range(i, f-1, -p):
            print(j, end=' ')
            sleep(1)


um_dez()
dez_zero()

ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = abs(int(input('Passo: ')))
cont(ini, fim, passo)
