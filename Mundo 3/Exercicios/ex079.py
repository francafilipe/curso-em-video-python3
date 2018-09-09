# Curso em Vídeo Python 3 - Exercicio 79
# Valores unicos em uma lista

valores = []

while True:
    valor = int(input('Digite um novo valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado. Não adicionado novamente.')

    des = ' '
    while des not in 'SN':
        des = str(input('Deseja continuar [s/n]? ')).upper()
    if des == 'N':
        break

print('-='*20)
valores.sort()
print('Foram digitados os valores {}'.format(valores))
