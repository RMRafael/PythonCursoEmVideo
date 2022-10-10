#Faça um programa em Python que abra e reproduza o aúdio de um arquivo MP3

import pygame
pygame.init()
#Colar arquivo mp3 na pasta e substituir Nome pelo nome do arquivo

pygame.mixer.music.load("nome")
pygame.mixer.music.play
pygame.event.wait()
