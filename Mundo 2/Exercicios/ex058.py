# Curso em Vídeo Python 3 - Exercicio 58
# Jogo de adivinhação v2.0

from random import randint

comp = randint(0, 10)
pess = -1
chutes = 0

print('{}JOGO ADIVINHAÇÂO{}'.format('-'*4, '-'*4))
while pess != comp:
    pess = int(input('Tente acertar o número: '))
    chutes += 1

print('-'*24)
print('Você venceu após {} tentativas.'.format(chutes))