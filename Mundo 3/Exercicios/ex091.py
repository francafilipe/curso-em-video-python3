# Curso em Vídeo Python 3 - Exercicio 91
# Jogo de dados em Python

from random import randint
from operator import itemgetter

jogs = {'jogador1': randint(1, 6),
        'jogador2': randint(1,6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

for k, v in jogs.items():
    print('O jogador {} rolou o valor {} no dado.'.format(k, v))

ranking = sorted(jogs.items(), key=itemgetter(1), reverse=True)
for i, j in enumerate(ranking):
    print('{}° lugar: {} com valor {}.'.format(i+1, j[0], j[1]))
