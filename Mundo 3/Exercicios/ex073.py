# Curso em Vídeo Python 3 - Exercicio 73
# Tuplas com times de futebol

times = ('São Paulo', 'Internacional', 'Flamengo', 'Palmeiras', 'Grêmio', 'Atletico Mineiro',
         'Cruzeiro', 'Corinthians', 'América Mineiro', 'Fluminense', 'Bahia', 'Botafogo',
         'Atletico Paranaense', 'Santos', 'Vasco', 'Vitória', 'Chapecoense', 'Sport', 'Ceara',
         'Paraná')

form = '-='*60
print('Classificação do Brasileirão: {}'.format(times))
print(form)
print('Classificados p/ Libertadores: {}'.format(times[0:6]))
print(form)
print('Rebaixados: {}'.format(times[-4:]))
print(form)
print('Listagem dos times em ordem alfabética: {}'.format(sorted(times)))
print(form)
print('A Chape esta na {}° posição.'.format(times.index('Chapecoense') + 1))

"""
for pos, time in enumerate(times):
    if time.upper() == 'CHAPECOENSE':
        posicao = pos + 1
        break
print('A Chape está na {}° posição.'.format(posicao))
"""