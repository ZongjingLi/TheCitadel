# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 10:03:22 2022

@author: 
"""
import eel
from citadel.interface import *

import pygame
#file = "src/KFT.mp3"
#pygame.mixer.init()
#music = pygame.mixer.music.load(file)

print("Start the Citadel...")

eel.init('/Users/melkor/Documents/GitHub/TheCitadel')
#pygame.mixer.music.play(loops=3)
eel.start('citadel/web/index.html')

