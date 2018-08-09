# Curso em Vídeo Python 3 - Exercicio 9
# Recebe um numero inteiro e mostra sua tabuada

num = int(input('Digite um número: '))
for i in range(11):
    print('{} x {} = {}'.format(num, i, num*i))
