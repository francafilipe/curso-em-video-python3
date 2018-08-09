# Curso em Vídeo Python 3 - Exercicio 36
# Aprovação e calculo de parcelas de empréstimo bancário

valor_casa = float(input('Insira o valor da casa: '))
anos = float(input('Insira em quantos anos deseja pagar: '))
salario = float(input('Salario mensal do comprador: '))

meses = anos*12
prest_mensal = valor_casa/meses

if prest_mensal > 0.3*salario:
    print('Infelizmente não há a possibilidade da realização de um empréstimo nesse valor.')
else:
    print('O empréstimo pode ser aprovado com uma parcela mensal de R${:.2f}'.format(prest_mensal))
