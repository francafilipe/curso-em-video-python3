# Curso em Vídeo Python 3 - Exercicio 40
# Calculo da media de um aluno e parecer final

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2

if media >= 7:
    print('APROVADO')
elif 5 <= media < 7:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')
