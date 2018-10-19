# Curso em Vídeo Python 3 - Exercicio 93
# Cadastro de Jogador de Futebol

jogador = dict()

tot_gols = 0
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))

for i in range(0, partidas):
    gol = int(input('Quantos gols na partida {}? '.format(i+1)))
    gols.append(gol)
    tot_gols += gol

jogador['gols'] = gols
jogador['total'] = tot_gols

print('-='*15)
print(jogador)

print('-='*15)
for k, v in jogador.items():
    print('O campo {} tem valor {}.'.format(k, v))

print('-='*15)
print('O jogador {} jogou {} partidas.'.format(jogador['nome'], partidas))
for i, g in enumerate(jogador['gols']):
    print('     Na partida {}, fez {} gols.'.format(i+1, g))
print('Total de {} gols.'.format(jogador['total']))
