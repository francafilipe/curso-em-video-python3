# Curso em Vídeo Python 3 - Exercicio 53
# Verificador de Palíndromo

frase = input('Insira a frase: ').lower().replace(' ', '')
invertida = ''

for i in range(len(frase) - 1, -1, -1):
    invertida += frase[i]
if frase == invertida:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')

