import pygame
import TextureLoader
import DrawHelper
import os

class GameScreen:
    # Load all of the textures and screen info (just not the "screen" itself)
    def __init__(self):
	    self.bgImage = TextureLoader.load(os.path.join('assets', 'game-bg.png'), (800,600))
		
    # Draw all screen elements here!
    def draw(self, screen):
    	if screen != 0:
            DrawHelper.drawAspect(screen,self.bgImage, 0,0)