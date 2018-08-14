# Curso em Vídeo Python 3 - Exercicio 68
# Jogo Par ou Impar

from random import randint

cont = 0
form = '-'*40

while True:
    computador = randint(0, 10)
    jogador_num = int(input('Informe o seu valor: '))
    total = computador + jogador_num

    jogador_pi = ''
    while jogador_pi != 'P' and jogador_pi != 'I':
        jogador_pi = str(input('Par ou Impar {P/I]: ')).strip().upper()

    if jogador_pi == 'P' and total % 2 == 0:
        print(f'Você jogou {jogador_num} e o computador jogou {computador}. Resultado {total} PAR.')
        print(f'Você VENCEU!')
        print(f'{form}')
        cont += 1
    elif jogador_pi == 'I' and total % 2 != 0:
        print(f'Você jogou {jogador_num} e o computador jogou {computador}. Resultado {total} IMPAR.')
        print(f'Você VENCEU!')
        print(f'{form}')
        cont += 1
    else:
        if computador % 2 == 0:
            res = 'PAR'
        else:
            res = 'IMPAR'
        print(f'Você jogou {jogador_num} e o computador jogou {computador}. Resultado {total} {res}.')
        print(f'Você PERDEU!')
        break

print(f'{form}')
print(f'GAME OVER! Você venceu {cont} vezes.')