# Curso em Vídeo Python 3 - Exercicio 44
# Calculo do valor de uma compra com diversas opções para pagamento

valor = float(input('Digite o valor da compra: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista no dinheiro
[ 2 ] À vista no cartão
[ 3 ] Dividido no cartão''')
pag = int(input())

if pag == 1:
    valor -= valor*0.1
    print('O valor final da compra é: {:.2f}'.format(valor))
elif pag == 2:
    valor = valor - valor*0.05
    print('O valor final da compra é: {:.2f}'.format(valor))
elif pag == 3:
    parc = int(input('Em quantas parcelas deseja realizar o pagamento? '))
    if parc == 1:
        valor = valor - valor * 0.05
        print('O valor final da compra é: {:.2f}'.format(valor))
    elif parc == 2:
        valor_parc = valor/parc
        print('O valor final da compra é: {:.2f}. Com parcelas com valor de: {:.2f}'.format(valor, valor_parc))
    else:
        valor += valor*0.2
        valor_parc = valor/parc
        print('O valro final da compra é: {:.2f}. Com parcelas no valor de: {:.2f}'.format(valor, valor_parc))
else:
    print('Opção inválida!')
