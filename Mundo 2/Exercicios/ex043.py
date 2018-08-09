# Curso em Vídeo Python 3 - Exercicio 43
# Calculo IMC e parecer

altura = float(input('Altura do usuário [m]: '))
massa = float(input('Massa (peso) do usuário [kg] :'))
imc = (massa / (altura ** 2))

if imc <= 18.5:
    print('O IMC do usuário é {:.2f}, sendo caracterizado como ABAIXO DO PESO.'.format(imc))
elif 18.8 < imc <= 25:
    print('O IMC do usuário é {:.2f}, sendo caracterizado como PESO IDEAL.'.format(imc))
elif 25 < imc <= 30:
    print('O IMC do usuário é {:.2f}, sendo caracterizado como SOBREPESO.'.format(imc))
elif 30 < imc <= 40:
    print('O IMC do usuário é {:.2f}, sendo caracterizado como OBESIDADE.'.format(imc))
else:
    print('O IMC do usuário é {:.2f}, sendo caracterizado como OBESIDADE MÓRBIDA.'.format(imc))
