# Curso em Vídeo Python 3 - Exercicio 76
# Lista de preços com Tupla

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Canetas', 22.30,
            'Livro', 34.90, 'Mochila', 120.30)

form = '-'*40
print(form)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print(form)

for pos in range(0, len(produtos), 2):
    print('{:.<30}'.format(produtos[pos]), end='')
    print('{:.>5} {:.2f}'.format('R$', produtos[pos + 1]))
