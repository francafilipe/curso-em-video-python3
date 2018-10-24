# Curso em Vídeo Python 3 - Exercicio 97
# Um print especial


def print_formatado(msg):
    tamanho = len(msg)
    linha = tamanho + 4
    print('~'*linha)
    print('{:^{}}'.format(msg, linha))
    print('~'*linha)


while True:
    msg = str(input())
    print_formatado(msg)
    des = str('Deseja continuar [S/N]? ').upper()
    if des == 'N':
        break
