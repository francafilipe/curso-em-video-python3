# Curso em Vídeo Python 3 - Exercicio 65
# Media, maior e menor valor dentre diversos numeros

soma = cont = maior = menor = 0
resp = 'S'
while resp != 'N':
    valor = int(input('Valor: '))
    if cont == 0:
        maior = valor
        menor = valor
    elif valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    soma += valor
    cont += 1
    resp = str(input('Deseja continuar a inserir valores [S/N]: ')).strip().upper()

media = soma / cont
print('Foram digitados {} valores, sendo a media dos valores igual a {}.'.format(cont, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
