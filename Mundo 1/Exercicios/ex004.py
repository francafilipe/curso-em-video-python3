# Curso em Vídeo Python 3 - Exercicio 4
# Programa que recebe algo digitado pelo usuario e apresenta informações sobre o tipo do dado entrado

entrada = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(entrada)))
print('Só tem espaços? {}'.format(entrada.isspace()))
print('É alfabético? {}'.format(entrada.isalpha()))
print('É alfanumérico? {}'.format(entrada.isalnum()))
print('Está em maiúsculas? {}'.format(entrada.isupper()))
print('Está em minúsculas? {}'.format(entrada.islower()))
print('Está capitalizada? {}'.format(entrada.istitle()))
