# Curso em Vídeo Python 3 - Exercicio 13
# Calculo do aumento recebido no salario de um funcionario

porc = 0.15  # Valor, em porcentagem, do aumento
sal_original = float(input('Digite o valor do salário do funcionário: '))
aumento = sal_original*porc  # Valor do aumento
sal_novo = sal_original + aumento  # Valor do novo salário, após o aumento
print('O salário do funcionário passará de {:.2f} para {:.2f}, sendo o aumento de {:.2f}.'
      .format(sal_original, sal_novo, aumento))
