# Curso em Vídeo Python 3 - Exercicio 103
# Ficha do Jogador


def jogador(nome='<desconhecido>', gols=0):
    print('O jogador {} fez {} gols no campeonato.'.format(nome, gols))


n = str(input('Nome do Jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    jogador(gols=g)
else:
    jogador(n,g)
