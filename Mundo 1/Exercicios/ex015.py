# Curso em vídeo Python 3 - Exercicio 15
# Calculo do valor do alguel de carro baseado nos dias e km

valor_diario = 60  # Valor por dia alugado
valor_km = 0.15  # Valor por km rodado
dias = int(input('Dias de aluguel: '))  # Recebe o valor de quantos dias o carro ficou alugado
km = float(input('Quantos kilometros foram rodados: '))  # Recebe o valor de km rodados com o carro

total = ((valor_diario*dias) + (valor_km*km))  # Calculo do valor total do aluguel do carro
print('O total a pagar é de R${:.2f}'.format(total))
