# Curso em Vídeo Python 3 - Exercicio 49
# Tabuada

num = int(input('Digite um número: '))

print('-='*8)
print('TABUADA DO {}'.format(num))
for i in range(0, 11):
    res = num*i
    print('{} x {:2} = {}'.format(num, i, res))
print('-='*8)
