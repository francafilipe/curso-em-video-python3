# Curso em Vídeo Python 3 - Exercicio 38
# Comparação entre dois numeros inteiros

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
    print('O primeiro valor ({}) é o maior.'.format(num1))
elif num2 > num1:
    print('O segundo valor ({}) é o maior.'.format(num2))
else:
    print('Os dois numeros são iguais.')
