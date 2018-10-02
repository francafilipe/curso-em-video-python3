# Curso em Vídeo Python 3 - Exercicio 84
# Lista composta e análise de dados

pessoas = []

while True:
    des = ' '
    dados = []

    nome = str(input('Digite o nome da pessoa: '))
    peso = float(input('Digite o peso da pessoa: '))
    dados.append(nome)
    dados.append(peso)

    pessoas.append(dados[:])

    while des not in 'SN':
        des = str(input('Deseja continuar [S/N]')).upper()
    if des == 'N':
        break

nome_maior = []
nome_menor = []

for i, pessoa in enumerate(pessoas):
    if i == 0:
        maior = menor = pessoa[1]
        nome_maior.append(pessoa[0])
    elif pessoa[1] == maior:
        nome_maior.append(pessoa[0])
    elif pessoa[1] == menor:
        nome_menor.append(pessoa[0])
    elif pessoa[1] > maior:
        nome_maior.clear()
        maior = pessoa[1]
        nome_maior.append(pessoa[0])
    elif pessoa[1] < menor:
        nome_menor.clear()
        menor = pessoa[1]
        nome_menor.append(pessoa[0])

print('Foram cadastradas {} pessoas.'.format(len(pessoas)))
print('O maior peso é de {} kg, sendo o peso de '.format(maior), end='')
for i, n in enumerate(nome_maior):
    if i != len(nome_maior) - 1:
        print(n, end=', ')
    else:
        print(n, end='.')

print('\nO menor peso é de {} kg, sendo o peso de '.format(menor), end='')
for i, n in enumerate(nome_menor):
    if i != len(nome_menor) - 1:
        print(n, end=', ')
    else:
        print(n, end='.')
