# Curso em Video Python 3 - Exercicio 102
# Função para calculo de um fatorial


def fatorial(n, show=False):
    """
    Função fatorial calcula o fatorial de um numero n passado como parâmetro.
    :param n: Valor do numero a ser calculado o fatorial;
    :param show: Se verdadeiro, mostra o procedimento de calculo realizado;
    :return: retorna o fatorial de n, se show for falso; se verdadeiro, retorna a linha de calculo com o resultado;
    """
    cont = ''
    res = 1
    for i in range(n, 0, -1):
        res = res*i
        if i > 1:
            cont += '{} x '.format(i)
        else:
            cont += '{} = {}'.format(i, res)
    if show:
        return cont
    else:
        return res


n = int(input('Insira um numero inteiro: '))
print(fatorial(n,show=True))
help(fatorial)
