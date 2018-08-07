# Curso em Vídeo Python 3 - Exercicio 21
# Abrir e reproduzir um arquivo MP3

import pygame  # Biblioteca pygame utilizada para criação de jogos em Python

pygame.init()  # inicializa a biblioteca
pygame.mixer.music.load('chap1.mp3')  # Carrega o arquivo no programa
pygame.mixer.music.play()  # Toca o audio do arquivo carregado
pygame.event.wait()  # Aguarda o final do audio para finalizar o programa
