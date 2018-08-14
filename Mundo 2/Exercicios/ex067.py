# Curso em Vídeo Python 3 - Exercicio 67
# Tabuada do valor inserido

while True:
    num = int(input('Insira o numero: '))
    if num < 0:
        break
    print('{}Tabuada do {}{}'.format('-'*3, num, '-'*3))
    for i in range (0, 11):
        print(f'{num} x {i} = {num * i}')
    print('-'*18)
