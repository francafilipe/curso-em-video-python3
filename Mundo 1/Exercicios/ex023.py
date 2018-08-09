# Curso em Vídeo Python 3 - Exercicio 23
# Recebe um numero de 0 a 9999 e imprime a unidade, dezena, centena e milhar separadamente

"""
numero = input('Digite um numero entre 0 e 9999: ')  # Recebe um valor numerico como string

print('unidade: {}'.format(numero[3]))  # Imprime o valor da unidade, posição 4 do numero
print('dezena: {}'.format(numero[2]))  # Dezena na posição 2
print('centena: {}'.format(numero[1]))  # Centena na posição 1
print('milhar: {}'.format(numero[0]))  # Milhar na posição 0

Programa apresenta a falha de não funcionar se o usuario digitar um numero 
abaixo de 1000 sem colocar os zeros a esquerda. Para isso usa-se uma solução
trabalhando com numeros inteiros e não strings.

"""

numero = int(input('Digite um numero entre 0 e 9999: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('unidade: {}'.format(unidade))
print('dezena: {}'.format(dezena))
print('centena: {}'.format(centena))
print('milhar: {}'.format(milhar))
