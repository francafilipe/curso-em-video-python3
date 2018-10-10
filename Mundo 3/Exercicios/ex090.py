# Curso em Vìdeo Python 3 - Exercicio 90
# Dicionario em Python

"""
nome = str(input('Nome: '))
media = float(input('Media: '))

if media >= 7:
    sit = 'Aprovado'
else:
    sit = 'Reprovado'

aluno = {'Nome': nome, 'Média': media, 'Situação': sit}

for k, v in aluno.items():
    print('{} é {}.'.format(k, v))
"""

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input('Média: '))

if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print('{} é {}.'.format(k, v))