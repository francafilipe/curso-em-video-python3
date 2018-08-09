# Curso em Vídeo Python 3 - Exercicio 25
# Verifica se há Silva no nome do usuario

nome = input('Digite o nome: ')  # Recebe o nome digitado pelo usuario
nome = nome.strip().lower()  # Coloca o nome em letras minusculas retirando os espaços no começo e final da string
valor = 'silva' in nome  # Verifica se há 'silva' na string nome. Retorna True se sim e False se não
print(valor)
