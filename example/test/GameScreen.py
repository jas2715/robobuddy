import pygame
import TextureLoader
import DrawHelper
import os

class GameScreen:
    # Load all of the textures and screen info (just not the "screen" itself)
    def __init__(self):
        self.bgImage = TextureLoader.load(os.path.join('assets', 'game-bg.png'), (800,600))
        self.botImage = TextureLoader.load(os.path.join('assets', 'bot.png'), (37,49))
        self.mainImage = TextureLoader.load(os.path.join('assets', 'main.png'), (151,151))
        self.funcImage = TextureLoader.load(os.path.join('assets', 'func.png'), (151,101))
        
    # Draw all screen elements here!
    def draw(self, screen):
    	if screen != 0:
            DrawHelper.drawAspect(screen,self.bgImage, 0,0)
            DrawHelper.drawAspect(screen,self.mainImage, 0.75,0.2)
            DrawHelper.drawAspect(screen,self.funcImage, 0.75,0.65)
            DrawHelper.drawAspect(screen,self.botImage, 0.365,0.835)
