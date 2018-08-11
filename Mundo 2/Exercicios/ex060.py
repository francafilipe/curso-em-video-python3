# Curso em Vídeo Python 3 - Exercicio 60
# Calculo de Fatorial


num = int(input('Digite o numero: '))
res = 1
while num != 0:
    res = res*num
    num -= 1
print(res)

"""
Resolução utilizando o laço for
num = int(input('Digite o numero: '))
res = 1
for i in range(num, 0, -1):
    res = res*i
print(res)
"""