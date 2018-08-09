# Curso em Vídeo Python 3 - Exercicio 11
# Calculo da quantidade de tinta para uma parede

lit = 2  # Cada litro de tinta pinta 2 m^2 de parede
larg = float(input('Digite a largura da parede: '))  # Recebe o valor da largura da parede
alt = float(input('Digite a altura da parede: '))  # Recebe o valor da altura da parede

area = larg*alt  # Calcula a area da parede
tinta = area/lit  # Calcula a quantidade de tinta gasta para a parede

print('É necessário {} litros de tinta para a pintura desta parede.'.format(tinta))
