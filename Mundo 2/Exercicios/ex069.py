# Curso em Vídeo Python 3 - Exercicio 69
# Cadastro de pessoas

form = '-'*40
cont_idade = cont_homem = cont_mulher = 0

while True:
    print('{}'.format(form))
    print('{:^40s}'.format('CADASTRE UMA PESSOA'))
    print('{}'.format(form))

    des = ''
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [H/M]: ')).strip().upper()

    if idade > 18:
        cont_idade += 1
    if sexo == 'H':
        cont_homem += 1
    if sexo == 'M' and idade < 20:
        cont_mulher += 1

    while des != 'S' and des != 'N':
        des = input('Deseja continuar [S/N]: ').strip().upper()
    if des == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {cont_idade}')
print(f'Total de homens cadastrados: {cont_homem}')
print(f'Total de mulheres com menos de 20 anos: {cont_mulher}')
