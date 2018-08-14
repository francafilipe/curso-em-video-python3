# Curso em Vídeo Python 3 - Exercicio 66
# Soma entre diversos números

num = soma = cont = 0
while True:
    num = int(input('Informe um número (digite 999 para parar): '))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
print(f'Foram digitados {cont} e soma entre eles é {soma}.')