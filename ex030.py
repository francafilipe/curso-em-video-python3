# Curso em Vídeo Python 3 - Exercicio 30
# Verificação se um numero inteiro digitado pelo usuario é par ou ímpar

num = int(input('Digite um número: '))
if num == 0:
    print('Zero não é par nem ímpar.')
elif num%2 == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')
