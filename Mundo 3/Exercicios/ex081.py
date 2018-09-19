# Curso em Vídeo Python 3 - Exercicio 81
# Extraindo dados de uma lista

valores = []

while True:
    des = ' '
    num = int(input("Insira um novo valor: "))
    valores.append(num)
    while des not in 'SN':
        des = str(input("Deseja continuar [S/N]? ")).upper()
    if des == 'N':
        break

valores.sort(reverse=True)
print('O número de valores digitados foi: {}'.format(len(valores)))
print('A lista ordenada de forma decrescente é: {}'.format(valores))
if 5 in valores:
    print('O valor 5 foi digitado e está na lista.')
else:
    print('O valor 5 não foi digitado e dessa forma não está na lista.')
