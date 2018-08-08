# Curso em Vídeo Python 3 - Exercicio 27
# Recebe o nome completo de uma pessoa e mostra o primeiro e ultimo nome

nome = input('Digite o nome completo: ')
nomes = nome.split()  # Coloca cada nome em uma lista separando por palavras
ultimo = len(nomes) - 1  # Ultimo nome é dado no ultimo index da lista, dado pelo tamanho desta - 1
print('primeiro: {}'.format(nomes[0]))  # Primeiro nome no index 0
print('ultimo: {}'.format(nomes[ultimo]))
