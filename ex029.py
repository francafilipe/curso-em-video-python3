# Curso em Vídeo Python 3 - Exercicio 29
# Verifica se a velocidade é superior ao limite 80km/h e se sim calcula a multa

vel = int(input('Digite a velocidade do carro: '))
if (vel > 80):
    print('Você foi multado!')
    multa = (vel-80)*7
    print('O valor da multa é {}.'.format(multa))
else:
    print('Não houve multa.')
