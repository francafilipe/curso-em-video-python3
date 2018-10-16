# Curso em Vídeo Python 3 - Exercicio 92
# Cadastro de Trabalhador em Python

from datetime import datetime

ano = datetime.now().year

cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['idade'] = ano - int(input('Ano de nascimento: '))
cadastro['ctps'] = int(input('Numero da carteira de trabalho [0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: '))
    cadastro['aposentadoria'] = cadastro['contratação'] + 35 - ano + cadastro['idade']

for k, v in cadastro.items():
    print('{}: {}.'.format(k, v))
