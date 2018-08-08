# Curso em Vídeo Python 3 - Exercicio 32
# Verificação se um ano é bissexto ou não

ano = int(input('Insira o ano: '))
if ano % 400 == 0:
    print('Ano bissexto.')
else:
    if ano % 4 == 0 and ano % 100 != 0:
        print('Ano bissexto.')
    else:
        print('Ano não bissexto.')

"""
Pode ser realizado em somente um comando if


ano = int(input('Insira o ano: '))
if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print('Ano bissexto.')
else:
    print('Ano não bissexto.')
"""