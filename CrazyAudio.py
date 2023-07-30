import pygame
from time import sleep
import random
pygame.mixer.init()

def QuackSound():
    sleep(1)
    pygame.mixer.music.load("quack-sound.mp3")
    pygame.mixer.music.play()

def LolSound():
    pygame.mixer.music.load("ImagineDragons-Symphony.mp")
    pygame.mixer.music.play()
    
def Boom():
    pygame.mixer.music.load("BoomHeadshotNOEFFECT.mp3")
    pygame.mixer.music.play()
    
def RickAstley():
    pygame.mixer.music.load("Rickiovec-Astleyovec.mp3")
    pygame.mixer.music.play()
    
def helicopter():
    pygame.mixer.music.load("HelicopterHelicopterParakoferSound.mp3")
    pygame.mixer.music.play()

SONGZ = [QuackSound, LolSound, Boom, RickAstley, helicopter]
Ransomizer = random.choice("SONGZ")

while True:
    print(randomizer)
        sleep(20)
        QuackSound()
        sleep(16)
        RickAstley()
        sleep(10)
        Boom()
        sleep(6)
        QuackSound()
        sleep(6)
        helicopter()
