# Curso em Vídeo Python 3 - Exercicio 72
# Número por extenso

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número (entre 0 e 20): '))
    if 0 <= numero <= 20:
        break
    print('Entrada inválida!')

print('Você digitou o número {}'.format(numeros[numero]))
