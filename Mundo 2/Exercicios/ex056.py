# Curso em Vídeo Python 3 - Exercicio 56
# Dados de 4 pessoas apresentando informações sobre idades

idade_total = 0
idade_velho = 0
mulheres_vinte = 0

for i in range(1, 5):
    print('{}{}°Pessoa{}'.format('-'*3, i, '-'*3))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    idade_total += idade
    if idade > idade_velho and sexo == 'M':
        idade_velho = idade
        nome_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres_vinte += 1

media_idade = idade_total / 4
print('A média de idade do grupo é de {} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(idade_velho, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres_vinte))
