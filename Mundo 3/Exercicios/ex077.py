# Curso em Vídeo Python 3 - Exercicio 77
# Contando vogais em Tupla

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Estudar',
            'Programador', 'Engenharia', 'Universidade', 'Computador')

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos as vogais: ', end='')
    for letra in palavra.lower():
        if letra in 'aeiou':
            print(letra, end=' ')
