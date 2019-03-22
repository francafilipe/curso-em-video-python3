# Curso em Vídeo Python 3 - Exercicio 104
# Validando entrada de dados em Python


def leiaint(msg):
    num = str(input(msg))
    while not num.isnumeric():
        print('ERRO! Digite um número válido.')
        num = str(input(msg))
    return int(num)


n = leiaint('Digite um número: ')
print('Você acabou de digitar o número {}'.format(n))
