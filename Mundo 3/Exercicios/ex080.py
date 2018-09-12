# Curso em Vídeo Python 3 - Exercicio 80
# Lista ordenada sem repetições

valores = []

for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    if i == 0:
        valores.append(valor)
    else:
        for j in range(0, len(valores)):
            if valor < valores[j]:
                valores.insert(j, valor)
                break
        else:
            valores.append(valor)
    print('Adicionado à posição {} da lista.'.format(valores.index(valor)))

print('Os valores adicionados, em ordem crescente, foram: {}'.format(valores))
