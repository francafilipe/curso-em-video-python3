# Curso em Vídeo Python 3 - Exercicio 19
# Sorteio do nome de um aluno dentre quatro

from random import randint  # Importa o metodo randint (gera um numero inteiro aleatorio da biblioteca random

aluno = {}  # Cria um dicionario vazio
for i in range(1, 5):  # Gera um loop com a variavel i percorrendo os valores de 1 a 4
    aluno[i] = input("Digite o nome do {}° aluno: ".format(i))  # Atribui cada nome digitado a um valor no dicionario

num = randint(1, 4)  # Gera um numero inteiro aleatório entre 1 e 4 (inclusive)
print('O aluno sorteado foi {}.'.format(aluno[num])) \
    # Imprime na tela o nome do aluno sorteado, acessando-o pelo sua chave no dict

"""
Outra maneira de resolver esse exercicio é utilizando-se o metodo .choice

from random import choice

aluno = [] #  Cria-se uma lista de alunos (ao inves de um dict)
for i in range(1, 5):
    aluno[i] = input("Digite o nome do {}° aluno: ".format(i))

escolhido = random.choice(aluno)  # Escolhe um dos elementos da lista aluno e atribiu esse valor a variavel escolhido
print('O aluno escolhido foi {}.'.format(escolhido)

"""
