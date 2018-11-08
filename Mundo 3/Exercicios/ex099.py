# Curso em Vídeo Python 3 - exercicio 99
# Maior numero


def fun_maior(nums):
    tam = len(nums)
    print('Foram passados {} numeros.'.format(tam))
    for i, v in enumerate(nums):
        if i == 0:
            maior = v
        elif v > maior:
            maior = v
    print('O maior valor entre os numeros é: {}'.format(maior))


num = list()
while True:
    des = ' '
    numero = int(input('Insira um valor: '))
    num.append(numero)
    while des not in 'SN':
        des = str(input('Deseja continuara a insirar valores [S/N]? ')).upper()
    if des == 'N':
        break
fun_maior(num)
