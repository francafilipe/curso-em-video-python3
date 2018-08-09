# Curso em Vídeo Python 3 - Exercicio 41
# Classificação de atletas em categorias referente a sua idade

from datetime import date

nasc = int(input('Ano de nascimento do atleta: '))
ano = date.today().year
idade = ano - nasc

if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SENIOR')
else:
    print('MASTER')
