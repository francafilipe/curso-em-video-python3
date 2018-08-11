# Curso em Vídeo Python 3 - Exercicio 62
# Termos de uma PA

prim_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = tot_termos = 0

while cont < 10:
    termo = prim_termo + cont*razao
    print('{}° termo: {}'.format(cont + 1, termo))
    cont += 1
    tot_termos += 1

des = int(input('Deseja mostrar mais quantos termos: '))
tot = tot_termos + des
while des != 0:
    while cont < tot:
        termo = prim_termo + cont*razao
        print('{}° termo: {}'.format(cont + 1, termo))
        cont += 1
        tot_termos += 1
    des = int(input('Deseja mostrar mais quantos termos: '))
    tot = tot_termos + des
