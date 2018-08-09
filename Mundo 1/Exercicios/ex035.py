# Curso em Vídeo Python 3 - Exercicio 35
# Verificação da existência de um triângulo

a = float(input('Digite o comprimento do primeiro lado: '))
b = float(input('Digite o comprimento do segundo lado: '))
c = float(input('Digite o comprimento do terceiro lado: '))
cond_a = abs(b - c) < a < (b + c)  # Analisa a condição de existência de um triângulo para o lado a
cond_b = abs(a - c) < b < (a + c)  # Analisa a condição de existência de um triângulo para o lado b
cond_c = abs(a - b) < c < (a + b)  # Analisa a condição de existência de um triângulo para o lado c

if cond_a and cond_b and cond_c:
    print('Os três lados podem formar um triângulo.')
else:
    print('Não é possível a formação de um triângulo.')
