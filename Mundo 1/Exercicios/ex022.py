# Curso em Vídeo Python 3 - Exercicio 22
# Informações de string sobre o nome completo de uma pessoa

nome = input('Digite seu nome completo: ')  # Recebe o nome completo da pessoa
nome_maiusc = nome.upper()  # Nome completo com letras maiusculas
nome_minusc = nome.lower()  # Nome completo com letras minusculas

nome_lista = nome.split()  # Divide o nome em palavras contidas em uma lista
nome_sem_esp = ''.join(nome.split())  # Une as palavras do nome sem espaços dentre elas
tam_completo = len(nome_sem_esp)  # Retorna o numero de letras que tem no nome completo (tamanho da string sem espaços)
tam_primeiro = len(nome_lista[0])  # Retorna o tamanho da primeira string na list ou seja o tamanho do primeiro nome

print(nome_maiusc)
print(nome_minusc)
print('O nome completo tem {} letras.'.format(tam_completo))
print('O primeiro nome tem {} letras.'.format(tam_primeiro))
