# Curso em Vídeo Python 3 - Exercicio 87
# Mais sobre Matrizes em Python

matriz = [[], [], []]
sum_pares = 0
sum_terceira = 0

for i in range(0, 3):
    for j in range(0, 3):
        num = int(input('Entre com o valor da posição [{} {}]: '.format(i, j)))
        matriz[i].append(num)

for i, vetor in enumerate(matriz):
    for j, valor in enumerate(vetor):
        if j != 2:
            print('[{}]'.format(valor), end=' ')
        else:
            print('[{}]'.format(valor))

        if valor % 2 == 0:
            sum_pares += valor
        if j == 2:
            sum_terceira += valor
        if i == 1:
            if j == 0:
                maior = valor
            elif valor > maior:
                maior = valor

print('A soma dos pares da matriz é igual a: {}'.format(sum_pares))
print('A soma dos valores da terceira coluna da matriz é igual a: {}'.format(sum_terceira))
print('O maior valor da segunda linha é: {}'.format(maior))
