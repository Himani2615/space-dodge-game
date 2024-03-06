# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 22:02:34 2023

@author: Himani
"""

import pygame
import time
import random

WIDTH,HEIGHT=1200,800
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Dodge")

def main():
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run=False
                break
            
    pygame.quit()
    
if __name__ == "__main__":
    main()
    
