# Curso em Vídeo Python 3 - Exercicio 37
# Conversão de um número inteiro para binário, hexadecimal ou octal

num = int(input('Digite o número: '))
base = int(input('Insira (1)binário, (2)octal e (3)hexadecimal: '))

if base == 1:
    print('O número {} em binário é: {}'.format(num, bin(num)))
elif base == 2:
    print('O número {} na base octal é: {}'.format(num, oct(num)))
elif base == 3:
    print('O número {} na base hexadecimal é: {}'.format(num, hex(num)))
