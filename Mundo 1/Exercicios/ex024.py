# Curso em Vídeo Python 3 - Exercicio 24
# Recebe o nome de uma cidade e verifica se ela começa com a palavra Santo

cidade = input('Digite o nome da cidade: ')  # Recebe o nome da cidade
cidade = cidade.strip().upper()  \
    # Remove espcaços indesejados inseridos pelo usuario (.strip()) e coloca todos os caracteres em maiusculo (.upper())

pos = cidade.find('SANTO')  # Retorna a posição onde a string 'SANTO' começa na string cidade
pos_bool = not bool(pos)  # Se 'SANTO' na posição 0 not bool retorna True, se em outra posição retorna False
print(pos_bool)
