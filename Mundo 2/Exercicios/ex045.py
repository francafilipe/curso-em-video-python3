# Curso em Vídeo Python 3 - Exercicio 45
# JOGO: Pedra, Papel e Tesoura

from random import randint

opcoes = {0: 'Pedra', 1: 'Papel', 2: 'Tesoura'}
print('''Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Sua jogada: '))
computador = randint(0, 2)

print('-='*20)
print('Sua jogada: {}'.format(opcoes[jogador]))
print('Jogada do computador: {}'.format(opcoes[computador]))
print('-='*20)

if jogador == computador:
    print('EMPATE! Ambos escolheram {}'.format(opcoes[jogador]))
elif jogador == 0:
    if computador == 1:
        print('COMPUTADOR VENCEU!')
    else:
        print('VOCÊ VENCEU!')
elif jogador == 1:
    if computador == 0:
        print('VOCÊ VENCEU!')
    else:
        print('COMPUTADOR VENCEU!')
elif jogador == 2:
    if computador == 0:
        print('COMPUTADOR VENCEU!')
    else:
        print('VOCÊ VENCEU!')
else:
    print('Entrada de jogada inválida!')
