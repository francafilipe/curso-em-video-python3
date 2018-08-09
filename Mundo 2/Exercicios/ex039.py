# Curso em Vídeo Python 3 - Exercicio 39
# Calculo do tempo que falta, ou que passou, para o alistamento militar

from datetime import date

ano_nasc = int(input('Insira o ano de nascimento do usuário: '))
ano = date.today().year
idade = ano - ano_nasc
if idade > 18:
    ano_pass = idade - 18
    print('Já passou o tempo de alistamento a {} anos.'.format(ano_pass))
elif idade < 18:
    ano_falt = 18 - idade
    print('Faltam {} anos para o alistamento.'.format(ano_falt))
else:
    print('Deve se alistar.')
