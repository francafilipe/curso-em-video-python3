# Cruso em Vídeo Python 3 - Exercicio 95
# Aprimorando Dicionarios

jogadores = list()

while True:
    jogador = dict()
    continuar = ' '
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

    jogadores.append(jogador.copy())

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).upper()
    if continuar == 'N':
        break

print('{:<5} {} {:>15} {:>20}'.format('Cód', 'Nome', 'Gols', 'Total'))
print('-'*48)
for i, jogador in enumerate(jogadores):
    print('{:^5} {:<15} {} {:^20}'.format(i, jogador['nome'], jogador['gols'], jogador['total']))

while True:
    dados = int(input('Inserir código do jogador para mostrar dados [999 encerrar]: '))
    if dados == 999:
        break
    elif dados > len(jogadores) - 1:
        print('Erro! Insira um código válido.')
    else:
        print(' -- Levantamento do jogador {}:'.format(jogadores[dados]['nome']))
        for jogo, gol in enumerate(jogadores[dados]['gols']):
            print('No jogo {} fez {} gols.'.format(jogo, gol))
