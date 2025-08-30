import pygame

# Substitua 'seuarquivo.mp3' pelo caminho do seu arquivo MP3
arquivo_mp3 = 'seuarquivo.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(arquivo_mp3)
pygame.mixer.music.play()

print("Reproduzindo áudio. Pressione Enter para parar.")
input()
pygame.mixer.music.stop()