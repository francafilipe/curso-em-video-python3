# Curso em Vídeo Python 3 - Exercicio 85
# Listas com pares e impares

pares = []
impares = []
numeros = [pares, impares]


for i in range(0, 7):
    num = int(input('Digite o {}° valor: '.format(i+1)))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()
print('Os valores pares digitados foram: {}'.format(numeros[0]))
print('Os valores impares digitados foram: {}'.format(numeros[1]))
