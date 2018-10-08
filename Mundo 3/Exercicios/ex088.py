# Curso em Vídeo Python 3 - Exercicio 88
# Palpites para Mega Sena

from random import randint

jogos = []
aux = []
palp = int(input('Quantos jogos a serem sorteados? '))

for j in range(0, palp):
    while True:
        num = randint(1, 60)
        if num not in aux:
            aux.append(num)
        if len(aux) == 6:
            break
    aux.sort()
    jogos.append(aux[:])
    aux.clear()
    print('Jogo {}: {}'.format(j+1, jogos[j]))
