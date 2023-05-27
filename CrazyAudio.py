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
    pygame.mixer.music.load("Boom Headshot NO EFFECT.mp3")
    pygame.mixer.music.play()
    
def RickAstley():
    pygame.mixer.music.load("Rickiovec-Astleyovec.mp3")
    pygame.mixer.music.play()
    
def helicopter():
    pygame.mixer.music.load("HelicopterHelicopterParakoferSound.mp3")
    pygame.mixer.music.play()

def SLEEPINGo():
    sleep(1)
def SLEEPINGtw():
    sleep(2)   
def SLEEPINGt():
    sleep(3)   
def SLEEPINGfo():
    sleep(4) 
def SLEEPINGf():
    sleep(5)
    
lossing = [sleep(1), SLEEPINGtw(), SLEEPINGt(), SLEEPINGf(), SLEEPINGfo()]
Lossing = random.choice(lossing)

def RandomPickTime():
    random.choice(Lossing)
    sleep(1)

SongsList = [helicopter(), RickAstley(), QuackSound(),Boom()]

def RandomPickSound():
    random.choice(SongsList)

while True:
        RandomPickTime()
        sleep(1)
        RandomPickSound()
