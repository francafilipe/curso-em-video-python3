# Curso em Vídeo Python 3 - Exercicio 89
# Boletim com listas compostas

alunos = []

while True:
    des = ' '
    notas = []
    aluno =[]

    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2

    notas.append(nota1)
    notas.append(nota2)

    aluno.append(nome)
    aluno.append(notas[:])
    aluno.append(media)
    notas.clear()
    alunos.append(aluno[:])
    aluno.clear()

    while des not in 'SN':
        des = str(input('Deseja continuar [S/N]? ')).upper()
    if des == 'N':
        break

for i, aluno in enumerate(alunos):
    print('{:} {:<3} {}'.format(i, aluno[0], aluno[2]))

while True:
    most = int(input('Mostrar nota de qual aluno? (999 interrompe) '))
    if most == 999:
        break
    else:
        print('Notas de {} são {}'.format(alunos[most][0], alunos[most][1]))
print(alunos)