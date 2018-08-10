# Curso em Vídeo Python 3 - Exercicio 48
# Soma de números ímpares multiplos de três até 500

soma = 0
for i in range(0, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
print('A soma dos números ímpares múltiplos de 3 até 500 é: {}.'.format(soma))
