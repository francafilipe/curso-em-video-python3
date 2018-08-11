# Curso em Vídeo Python 3 - Exercicio 63
# Sequencia de fibonacci

n = abs(int(input('Digite o numero de elementos da sequência: ')))

if n == 1:
    print(0)
elif n == 2:
    print(0, 1)
else:
    elem = 3
    ult_valor = 1
    pen_valor = 0
    print(0, 1, end=' ')
    while elem <= n:
        valor = ult_valor + pen_valor
        print('{}'.format(valor), end=' ')
        pen_valor = ult_valor
        ult_valor = valor
        elem += 1
