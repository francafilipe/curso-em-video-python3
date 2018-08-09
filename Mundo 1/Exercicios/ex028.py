# Curso em Vídeo Python 3 - Exercicio 28
# Jogo de adivinhação de um numero inteiro de 0 a 1

from random import randint

numero = randint(0, 5)
print(numero)
chute = int(input('Chute um número de 0 a 5: '))
if (chute == numero):
    print('Parabéns, você acertou o número!')
else:
    print('Opa! Essa não era o número correto.')
