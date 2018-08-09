# Curso em Vídeo Python 3 - Exercicio 42
# Verificação da existência de um triângulo

a = float(input('Digite o comprimento do primeiro lado: '))
b = float(input('Digite o comprimento do segundo lado: '))
c = float(input('Digite o comprimento do terceiro lado: '))
cond_a = abs(b - c) < a < (b + c)  # Analisa a condição de existência de um triângulo para o lado a
cond_b = abs(a - c) < b < (a + c)  # Analisa a condição de existência de um triângulo para o lado b
cond_c = abs(a - b) < c < (a + b)  # Analisa a condição de existência de um triângulo para o lado c

if not(cond_a and cond_b and cond_c):
    print('Não é possível a formação de um triângulo.')
elif a == b and a == c:
    print('Triângulo equilátero.')
elif a == b or a == c or b == c:
    print('Triângulo isóceles.')
else:
    print('Triângulo escaleno.')
