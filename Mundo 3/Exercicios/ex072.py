# Curso em Vídeo Python 3 - Exercicio 72
# Número por extenso

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um número (entre 0 e 20): '))

while 20 < numero < 0:
    numero = int(input('Entrada inválida. Digite um número (entre 0 e 20): '))

print('Você digitou o número {}'.format(numeros[numero]))
