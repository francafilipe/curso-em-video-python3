# Curso em Vídeo Python 3 - Exercicio 18
# Seno, cosseno e tangente de um angulo

from math import cos, sin, tan, radians

angulo = float(input('Insira um angulo em graus: '))  # Recebe o valor do angulo em graus
angulo = radians(angulo)
cosseno = cos(angulo)  # Calcula o valor do cosseno do angulo
seno = sin(angulo)  # Calcula o valor do seno do angulo
tang = tan(angulo)  # Calcula o valor da tangente do angulo

print('O angulo {:.2f}rad tem cosseno igual a {:.2}, seno igual a {:.2} e tangente igual a {:.2}.'
      .format(angulo, cosseno, seno, tang))
