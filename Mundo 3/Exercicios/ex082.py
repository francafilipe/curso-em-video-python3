# Curso em Vídeo Python 3 - Exercicio 82
# Dividindo valores em várias listas

valores = []

while True:
    des = ' '
    num = int(input('Insira um novo numero: '))
    valores.append(num)
    while des not in 'SN':
        des = str(input('Deseja continuar [S/N]? ')).upper()
    if des == 'N':
        break

valores.sort()
pares = []
impares = []

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

pares.sort()
impares.sort()

print('A lista de valores ditados é: {}'.format(valores))
print('Os valores pares são: {}'.format(pares))
print('Os valores impares são: {}'.format(impares))
