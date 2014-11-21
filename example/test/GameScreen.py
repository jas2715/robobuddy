import pygame
import TextureLoader
import DrawHelper
import os

class GameScreen:
    # Load all of the textures, fonts, titles, etc.
    def __init__(self):
        self.bgImage = TextureLoader.load(os.path.join('assets', 'game-bg.png'), (800,600))
        self.botImage = TextureLoader.load(os.path.join('assets', 'bot.png'), (37,49))
        self.mainImage = TextureLoader.load(os.path.join('assets', 'main.png'), (151,151))
        self.funcImage = TextureLoader.load(os.path.join('assets', 'func.png'), (151,101))
        self.titleFont =  pygame.font.SysFont('ActionIsShaded', 48)
        self.labelFont = pygame.font.SysFont('ActionIsShaded', 24)
        
    # Draw all screen elements here!
    def draw(self, screen):
    	if screen != 0:
            # Images
            DrawHelper.drawAspect(screen,self.bgImage, 0,0)
            DrawHelper.drawAspect(screen,self.mainImage, 0.75,0.2)
            DrawHelper.drawAspect(screen,self.funcImage, 0.75,0.5)
            DrawHelper.drawAspect(screen,self.botImage, 0.365,0.835)

            # Text blocks
            title1 = self.titleFont.render("Robobuddy", 1, (10,10,10))
            title1pos = title1.get_rect()
            title1pos.centerx = 675
            title1pos.centery = 50
            screen.blit(title1, title1pos)

            labelMain = self.labelFont.render("main:", 1, (10,10,10))
            labelFunc = self.labelFont.render("f:", 1, (10,10,10))
            mainPos = labelMain.get_rect()
            funcPos = labelFunc.get_rect()
            mainPos.centerx = 570
            funcPos.centerx = 585
            mainPos.centery = 140
            funcPos.centery = 325
            screen.blit(labelMain, mainPos)
            screen.blit(labelFunc, funcPos)

            labelEq = self.labelFont.render("<insert equation here>", 1, (10,10,10))
            eqPos = labelEq.get_rect()
            eqPos.centerx = 200
            eqPos.centery = 50
            screen.blit(labelEq, eqPos)
            
