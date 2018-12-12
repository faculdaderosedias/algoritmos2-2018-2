#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import  pyautogui
import pygame
from pygame.locals import *


# Constantes
WIDTH = 800
HEIGHT = 600


# Clases
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PyGame Tutorial")
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
                return 0

if __name__ == '__main__':
    pygame.init()
    main()
