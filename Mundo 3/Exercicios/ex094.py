# Curso em Vídeo Python 3 - Exercicio 94
# Unindo dicionários e listas

pessoas = list()
tot_idade = 0

while True:
    des = ' '
    sexo = ' '
    pessoa = dict()

    pessoa['nome'] = str(input('Nome: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper()
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))

    tot_idade += pessoa['idade']

    pessoas.append(pessoa.copy())
    pessoa.clear()

    while des not in 'SN':
        des = str(input('Deseja continuar? [S/N] ')).upper()
    if des == 'N':
        break

print('=-'*40)
media = tot_idade/len(pessoas)

mulheres = list()
media_acima = list()
media_abaixo = list()

for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    if pessoa['idade'] >= media:
        media_acima.append(pessoa)
    else:
        media_abaixo.append(pessoa)

print('A) Ao todos temos {} pessoas cadastradas.'.format(len(pessoas)))
print('B) A média de idades é de {:.2f} anos.'.format(media))
print('C) As mulheres cadastradas foram ', end='')
for i, m in enumerate(mulheres):
    if i != len(mulheres) - 1:
        print(m, end=', ')
    else:
        print(m, end='.')
print('D) Lista das pessoas que estão acima da média de idade:')
for pessoa in media_acima:
    print('    Nome: {}; sexo = {}; idade = {}'.format(pessoa['nome'], pessoa['sexo'], pessoa['idade']))
