# Curso em Vídeo Python 3 - Exercicio 12
# Calculo de desconto no preço de um produto

porc = 0.05  # Valor de 5% de desconto (em decimal)
val_original = float(input('Digite o valor do produto: '))
desc = val_original*porc  # Calcula o valor do desconto do preço
val_novo = val_original - desc  # Calcula o novo valor do produto
print('O produto passou do valor de {:.2f} para {:.2f}. \nO desconto dado foi de {:.2f} '
      .format(val_original, val_novo, desc))
