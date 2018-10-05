# Curso em Vídeo Python 3 - Exercicio 86
# Matriz em Python

matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        num = int(input('Insira o valor da posição [{}, {}]: '.format(i, j)))
        matriz[i].append(num)

for vetor in matriz:
    for i, valor in enumerate(vetor):
        if i != 2:
            print('[{}]'.format(valor), end=' ')
        else:
            print('[{}]'.format(valor))
