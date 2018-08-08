# Curso em vídeo Python 3 - Exercicio 26
# Contagem da letra 'a' em uma frase

frase = input('Digite uma frase: ')
frase = frase.strip().lower()  # Coloca a frase em minusculas retirando os espaços indesejados no começo e final

a_vezes = frase.count('a')  # Conta o numero de vezes que 'a' aparece na string frase
a_primeiro = frase.find('a')  # Posição da primeira vez que 'a' ocorre na string frase
a_ultimo = frase.rfind('a')  # Posição da ultima vez que 'a' ocorre na string frase (procura a começando pela direita)

print('A letra a aparece na frase {} vezes.'.format(a_vezes))
print('A primeira vez na posição {} e ultima na posição {}.'.format(a_primeiro, a_ultimo))
