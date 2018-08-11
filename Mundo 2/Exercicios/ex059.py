# Curso em Vídeo Python 3 - Exercicio 59
# Calculadora básica

print('{}CALCULADORA{}'.format('-'*6, '-'*6))
num1 = float(input('Primeiro valor: '))
num2 = float(input('Segundo valor: '))
opc = 0

while opc != 5:
    print('''OPERAÇÕES
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NUMEROS
    [ 5 ] SAIR''')
    opc = int(input('Opção: '))

    if opc == 1:
        soma = num1 + num2
        print('A soma dos numeros é: {}'.format(soma))
    elif opc == 2:
        mult = num1 * num2
        print('O produto dos numeros é: {}'.format(mult))
    elif opc == 3:
        if num1 > num2:
            print('O maior numero é: {}'.format(num1))
        elif num1 < num2:
            print('O maior numero é: {}'.format(num2))
        else:
            print('Os numeros são iguais: {}'.format(num1))
    elif opc == 4:
        num1 = float(input('Primeiro valor: '))
        num2 = float(input('Segundo valor: '))
    elif opc == 5:
        print('Fechando programa...')
    else:
        print('Opção inválida')
    print('-'*23)
