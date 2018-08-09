# Curso em Vídeo Python 3 - Exercicio 37
# Conversão de um número inteiro para binário, hexadecimal ou octal

num = int(input('Digite o número: '))
base = int(input('''Insira a base desejada para conversão:
( 1 ) Binário
( 2 ) Octal
( 3 ) Hexadecimal\n'''))

if base == 1:
    print('O número {} em binário é: {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('O número {} na base octal é: {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('O número {} na base hexadecimal é: {}'.format(num, hex(num)[2:]))
