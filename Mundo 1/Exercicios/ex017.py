# Curso em Vídeo Python 3 - Exercicio 17
# Calculo da hipotenusa de um triângulo retangulo

from math import hypot

cat_op = float(input('Valor do cateto oposto: '))  # Recebe o valor do cateto oposto do triangulo
cat_adj = float(input('Valor do cateto adjacente: '))  # Recebe o valor do cateto adjacente do triangulo
hip = hypot(cat_op, cat_adj)  # Calcula o valor da hipotenusa pelo teorema de Pitagoras
print('O valor da hipotenusa do triangulo é {:.2}'.format(hip))
