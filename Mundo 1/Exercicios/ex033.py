# Curso em Vídeo Python 3 - Exercicio 33
# Maior entre três numeros digitados

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2:
    if n1 > n3:
        print('O primeiro número é o maior: {}'.format(n1))
    else:
        print('O terceiro número é o maior: {}'.format(n3))
else:
    if n2 > n3:
        print('O segundo número é o maior: {}'.format(n2))
    else:
        print('O terceiro número é o maior: {}'.format(n3))
