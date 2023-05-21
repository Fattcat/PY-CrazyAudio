import pygame
from time import sleep
import pyautogui as pg
import random
pygame.mixer.init()

def QuackSound():
    pygame.mixer.music.load("quack-sound.mp3")
    pygame.mixer.music.play()

def SLEEPINGo():
    sleep(10)

def SLEEPINGtw():
    sleep(5)
    
def SLEEPINGt():
    sleep(50)
    
def SLEEPINGfo():
    sleep(3)
    
def SLEEPINGf():
    sleep(21)

lossing = [SLEEPINGo(), SLEEPINGtw(), SLEEPINGt(), SLEEPINGf(), SLEEPINGfo()]
Lossing = random.randint(lossing)

def RandomPick():
    random.choice(lossing)


while True:
        QuackSound()
        RandomPick()
