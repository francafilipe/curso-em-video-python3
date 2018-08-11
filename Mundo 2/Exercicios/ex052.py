# Curso em Vídeo Python 3 - Exercicio 52
# Numeros primos

print('{}NUMEROS PRIMOS{}'.format('-='*3, '-='*3))
num = abs(int(input('Insira o numero: ')))

if num == 0 or num == 1:
    print('Não é um numero primo.')
elif num == 2:
    print('É primo.')
elif num % 2 == 0 and num != 2:
    print('Não é numero primo.')
else:
    for i in range(3, num):
        div = num % i
        if div == 0:
            print('Não é primo')
            break
    else:
        print('É primo')

"""
Solução alternativa

print('{}NUMEROS PRIMOS{}'.format('-='*3, '-='*3))
num = abs(int(input('Insira o numero: ')))
total = 0
for i in range(1, num + 1):
    if num % i == 0:
        total += 1

print('O numero {} foi divisivel {} vezes.'.format(num, total))
if total == 2:
    print('O numero É PRIMO')
else: 
    print('O numero NÃO É PRIMO')
    
"""