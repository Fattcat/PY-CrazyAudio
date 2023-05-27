import pygame
from time import sleep
import pyautogui as pg
import random
pygame.mixer.init()

def QuackSound():
    sleep(1)
    pygame.mixer.music.load("quack-sound.mp3")
    pygame.mixer.music.play()

#def LolSound():
#    pygame.mixer.music.load("ImagineDragons-Symphony.mp")
#    pygame.mixer.music.play()
    
def Boom():
    pygame.mixer.music.load("BoomHeadshotNOEFFECT.mp3")
    pygame.mixer.music.play()
    
def RickAstley():
    pygame.mixer.music.load("Rickiovec-Astleyovec.mp3")
    pygame.mixer.music.play()
    
def helicopter():
    pygame.mixer.music.load("HelicopterHelicopterParakoferSound.mp3")
    pygame.mixer.music.play()

while True:
        sleep(1)
        QuackSound()
        sleep(16)
        RickAstley()
        sleep(6)
        Boom()
        sleep(6)
        QuackSound()
        sleep(6)
        helicopter()
