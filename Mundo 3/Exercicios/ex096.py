# Curso em Vídeo Python 3 - Exercicio 96
# Dimensões de um terreno


def area_terreno(larg, comp):
    area = larg*comp
    print('A area do terreno de {}x{} é de {} m².'.format(larg, comp, area))


larg = float(input('Largura [m]: '))
comp = float(input('Comprimento [m]: '))
area_terreno(larg, comp)
