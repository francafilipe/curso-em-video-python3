# Curso em Vídeo Python 3 - Exercicio 50
# Soma dos numeros pares

soma = 0
for i in range(6):
    num = int(input('Digite o {}° numero: '.format(i+1)))
    if num % 2 == 0:
        soma += num
print('A soma dos números pares é: {}'.format(soma))
