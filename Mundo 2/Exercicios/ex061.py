# Curso em Vídeo Python 3 - Exericio 61
# Dez primeiros termos de um PA

prim_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0

while cont < 10:
    termo = prim_termo + cont*razao
    print('{}° termo: {}'.format(cont + 1, termo))
    cont += 1
