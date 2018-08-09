# Curso em Vídeo Python 3 - Exercicio 34
# Calculo do aumento do salario de um funcionario

salario = float(input('Digite o salário do funcionário: '))
if salario > 1250:
    aumento = salario*0.1
    salario_novo = salario + aumento
else:
    aumento = salario*0.15
    salario_novo = salario + aumento

print('O novo salário é de: {} \nResultando um aumento de: {}'.format(salario_novo, aumento))
