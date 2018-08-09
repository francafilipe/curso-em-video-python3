# Curso em Vídeo Python 3 - Exercicio 16
# Parte inteira de um numero real

from math import trunc

num = float(input('Digite um numero: '))  # Recebe um valor digitado pelo usuario
num_int = trunc(num)  # Toma somente a parte inteira de um numero
print('A parte inteira do numero {:.3f} é {}'.format(num, num_int))
