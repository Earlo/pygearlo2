import os
import pygame
import __main__

BASEPATH = os.path.dirname(os.path.realpath(__main__.__file__))

LANGUAGE = "english"

# SWIDTH =  800
# SHEIGTH = 600

# 640*896 ?
GWIDTH = 640
GHEIGTH = 900
SWIDTH = GWIDTH + 20
SHEIGTH = GHEIGTH + 20

FONT = "Calibri"

# millisecnds
LETTER_INPUT_HELD_DOWN_DELAY = 100
LETTER_INPUT_HELD_DOWN_INTERWAL = 20
INPUT_BOX_ACTIVITY_INDICATOR = "|"

SCREENUPDATEEVENT = pygame.USEREVENT + 1
FUNCTIONCALLEVENT = pygame.USEREVENT + 2
UPDATEONTICKEVENT = pygame.USEREVENT + 3


def nothing():
    pass
