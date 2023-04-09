# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 10:03:22 2022

@author: 
"""
import eel
from citadel import *
from config import *

import pygame

# start to play the intro music of the Citadel
file = "citadel/web/src/KFT.mp3"
pygame.mixer.init()
music = pygame.mixer.music.load(file)

# start to load the Ice Crown Citadel
from icc.reflection.domains.arithmetics import *
CitadelInterface = TheCitadelInterface(config)
#e = CitadelInterface.solution_abstraction()


print("Start the Citadel...")

# play the music of the ice crown citadel

pygame.mixer.music.play(loops=3)
eel.init('/Users/melkor/Documents/GitHub/TheCitadel')
# start the eel web page.
eel.start('citadel/web/icecrown_citadel.html')

