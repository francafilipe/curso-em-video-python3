# Curso em Vídeo Python 3 - Exercicio 23
# Recebe um numero de 0 a 9999 e imprime a unidade, dezena, centena e milhar separadamente

numero = input('Digite um numero entre 0 e 9999: ')  # Recebe um valor numerico como string

print('unidade: {}'.format(numero[3]))  # Imprime o valor da unidade, posição 4 do numero
print('dezena: {}'.format(numero[2]))  # Dezena na posição 2
print('centena: {}'.format(numero[1]))  # Centena na posição 1
print('milhar: {}'.format(numero[0]))  # Milhar na posição 0
