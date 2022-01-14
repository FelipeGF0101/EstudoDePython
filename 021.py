"""
Faça um programa em Python que abra e reproduza o ádiu de um arquivo MP3

# Copie o arquivo para a pasta do projeto

# Resolução do Guanabara.
Não funcionou aqui!

import pygame
# O pygame precisa ser iniciado
pygame.init()
pygame.mixer.music.load('02 - Dream On.mp3')
pygame.mixer.music.play()
# O programa precisa esperar o evento terminar para poder encerrar o programa. 
pygame.event.wait()

"""
# Forma mais simples que encontrei

from playsound import playsound
playsound("demo_2.mp3")
