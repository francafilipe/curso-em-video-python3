# Curso em Vídeo Python 3 - Exercicio 71
# Simulador de caixa eletrônico

form = '-'*40

print(form)
print('{:^40}'.format('BANCO CEV'))
print(form)
valor = total = int(input('Qual valor a ser sacado: R$'))
ced = 50

while True:
    total_ced = total // ced
    total = total % ced
    print('Total de {} cédulas de R${}'.format(total_ced, ced))

    if ced == 50:
        ced = 20
    elif ced == 20:
        ced = 10
    elif ced == 10:
        ced = 1
    else:
        break
print(form)