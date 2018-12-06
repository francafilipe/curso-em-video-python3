# Curso em vídeo Python 3 - Exercicio 101
# Funçoes para votação


def voto(nasc):

    from datetime import date
    now = date.today()

    idade = now.year - nasc
    if 0 < idade < 16:
        return 'Idade de {} anos. NÃO VOTA.'.format(idade)
    elif 16 <= idade < 18 or idade >=60:
        return 'Idade de {} anos. VOTO OPCIONAL.'.format(idade)
    elif 18 <= idade < 60:
        return 'Idade de {} anos. VOTO OBRIGATÓRIO.'.format(idade)
    else:
        return 'Ano de nascimento inserio não válido.'


nasc = int(input('Ano de nascimento: '))
print(voto(nasc))
