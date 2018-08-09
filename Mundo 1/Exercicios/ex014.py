# Curso em Vídeo Python 3 - Exercicio 14
# Conversão de graus Celsius para Fahrenheit

celsius = float(input('Digite um valor em graus Celsius: '))  # Recebe um valor digitado em graus Calsius
fahr = ((celsius*1.8) + 32)  # Equação para conversão do valor em Celsius para Fahrenheit
print('A temperatura de {:.2f}°C corresponde a {:.2f}°F.'.format(celsius, fahr))
