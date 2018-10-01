# Curso em Vídeo Python 3 - Exercicio 83
# Validando expresões matematicas

expr = str(input('Insira a expressão matematica: '))
cont1 = cont2 = 0

for car in expr:
    if car == '(':
        cont1 += 1
    if car == ')':
        cont2 += 1

if cont1 == cont2:
    print('Expressão válida!')
else:
    print('Expressão invàlida!')
