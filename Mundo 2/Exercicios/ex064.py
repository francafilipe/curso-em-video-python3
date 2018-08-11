# Curso em Vídeo Python 3 - Exercicio 64
# Soma de varios numeros

parada = soma = cont = 0

while parada != 999:
    num = int(input('Numero: '))
    parada = num
    soma += num
    cont += 1

print('Foram digitados {} numeros.'.format(cont))
print('A soma dos numeros é igual a: {}'.format(soma-parada))
