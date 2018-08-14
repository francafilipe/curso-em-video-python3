# Curso em Vídeo Python 3 - Exercicio 64
# Soma de varios numeros

soma = cont = 0
num = int(input('Numero: '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Numero: '))

print('Foram digitados {} numeros.'.format(cont))
print('A soma dos numeros é igual a: {}'.format(soma))
