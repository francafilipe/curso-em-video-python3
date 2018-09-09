# Curso em Vídeo Python 3 - Exercicio 78
# Maior e menor valor em uma lista

valores = []

for i in range(0, 5):
    valores.append(int(input(f'Insira o {i+1}° valor: ')))

for c, v in enumerate(valores):
    if c == 0:
        maior = v
        menor = v
        posM = posm = c
    else:
        if v > maior:
            maior = v
        elif v < menor:
            menor = v

posM = [c for c, v in enumerate(valores) if v == maior]
posm = [c for c, v in enumerate(valores) if v == menor]
print('Os valores digitados foram: {}'.format(valores))
print('O maior valor digitado foi {} nas posições {}'.format(maior, posM))
print('O menor valor digitado foi {} nas posições {}'.format(menor, posm))
