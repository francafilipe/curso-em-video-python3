# Curso em Vìdeo Python 3 - Exercicio 70
# Estatisticas em produtos

form = '-'*40
total = mais_mil = cont = 0

print('{:^40}'.format('LISTA DE COMPRAS'))
print(f'{form}')

while True:
    resp = ''
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço: R$'))
    total += valor
    cont += 1

    if valor > 1000:
        mais_mil += 1
    if cont == 1:
        mais_barato = nome
        valor_mb = valor
    elif valor < valor_mb:
        mais_barato = nome
        valor_mb = valor

    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if resp == 'N':
        break

print('{}FIM DO PROGRAMA{}'.format('-'*17, '-'*17))
print
print('O total da compra foi de {:.2f}.'.format(total))
print('Há {} produtos custando mais de R$1000.'.format(mais_mil))
print('O produto mais barato foi {} custando R${}.'.format(mais_barato, valor_mb))
