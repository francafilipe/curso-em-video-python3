# Curso em Vídeo Python 3 - Exercicio 51
# Progressão Aritmética

print('{}Progressão Aritmética{}'.format('-='*3, '-='*3))
prim = int(input('Primeiro termo: '))
raz = int(input('Razão: '))

for i in range(0, 10):
    termo = prim + i*raz
    print('{}° termo: {}'.format(i+1, termo))

