# Curso em Vídeo Python 3 - Exercicio 55
# Maior e menor peso

maior = 0
menor = 0

for i in range(0, 5):
    peso = float(input('Digite o peso da {}° pessoa: '.format(i+1)))
    if peso > maior:
        maior = peso
    if i == 0:
        menor = peso
    elif peso < menor:
        menor = peso

print('O maior peso é: {}'.format(maior))
print('O menor peso é: {}'.format(menor))
