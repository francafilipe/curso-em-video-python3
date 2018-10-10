# Curso em Vídeo Python 3 - Exercicio 89
# Boletim com listas compostas

alunos = []

while True:
    des = ' '
    notas = []
    aluno = []

    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2

    notas.append(nota1)
    notas.append(nota2)
    alunos.append([nome, notas[:], media])

    notas.clear()

    while des not in 'SN':
        des = str(input('Deseja continuar [S/N]? ')).upper()
    if des == 'N':
        break

print('-='*20)
print('{:<3} {:<10} {:>10}'.format('N°', 'Nome', 'Média'))
print('-'*25)
for i, aluno in enumerate(alunos):
    print('{:<3} {:<10} {:>9}'.format(i, aluno[0], aluno[2]))

while True:
    print('-' * 25)
    most = int(input('Mostrar nota de qual aluno? (999 interrompe) '))
    if most == 999:
        break
    else:
        print('Notas de {} são {}'.format(alunos[most][0], alunos[most][1]))
print('{:<14}FINALIZADO{:>14}'.format('-='*7, '-='*7))
