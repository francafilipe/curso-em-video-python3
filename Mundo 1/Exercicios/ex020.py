# Curso em Vídeo Python 3 - Exercicio 20
# Gera uma lista aleatoria da ordem de alunos

from random import shuffle  # Importa o metodo shuffle da biblioteca random

alunos = []  # Cria uma lista vazia chamada alunos
for i in range(1,5):  # Loop onde a variavel i percorre os valores de 1 a 4
    alunos.append(input('Digite o nome do {}° aluno: '.format(i)))  \
        # Insere o nome do aluno digitado pelo usuario a lista

shuffle(alunos)  # Embaralha a ordem da lista aluno de forma pseudo aleatoria
print('A ordem dos alunos é: {}, {}, {} e {}.'.format(alunos[0], alunos[1], alunos[2], alunos[3]))
