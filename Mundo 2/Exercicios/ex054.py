# Curso em Vídeo Python 3 - Exercicio 54
# Contador de maioridade

from datetime import date

cont_maior = 0
cont_menor = 0
ano_atual = date.today().year

for i in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = ano_atual - ano
    if idade >= 21:
        cont_maior += 1
    else:
        cont_menor += 1
print('{} pessoas já atingiram a maioridade.'.format(cont_maior))
print('{} pessoas ainda não atingiram a maioridade.'.format(cont_menor))
