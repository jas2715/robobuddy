import pygame
import TextureLoader
import DrawHelper
import math
import os
from GameTile import GameTile

tileImages = []
tiles = []

class GameScreen:
    # Load all of the textures, fonts, titles, etc.
    def __init__(self):
        self.bgImage = TextureLoader.load(os.path.join('assets', 'game-bg.png'), (800,600))
        self.botImage = TextureLoader.load(os.path.join('assets', 'bot.png'), (37,49))
        self.mainImage = TextureLoader.load(os.path.join('assets', 'main.png'), (151,151))
        self.funcImage = TextureLoader.load(os.path.join('assets', 'func.png'), (151,101))

        # Load tile images
        for i in range(0, 5):
            tileImages.append(TextureLoader.load(os.path.join('assets', 'tile' + str(i+1) + '.png'), (47,47) ))

        #self.tileImage1 = TextureLoader.load(os.path.join('assets', 'tile1.png'), (47,47))
        #self.tileImage2 = TextureLoader.load(os.path.join('assets', 'tile2.png'), (47,47))
        #self.tileImage3 = TextureLoader.load(os.path.join('assets', 'tile3.png'), (47,47))
        #self.tileImage4 = TextureLoader.load(os.path.join('assets', 'tile4.png'), (47,47))
        #self.tileImage5 = TextureLoader.load(os.path.join('assets', 'tile5.png'), (47,47))

        # The selected tile is the one being dragged
        self.selectedTile = None

        # Initialize tiles with their images & positions
        for j in range(0,5):
            tiles.append(GameTile(tileImages[j], 600+j*5, 500))

        # Two sizes of the same font to use
        self.titleFont =  pygame.font.SysFont('ActionIsShaded', 48)
        self.labelFont = pygame.font.SysFont('ActionIsShaded', 24)

    # Update the game logic
    def update(self):
        if self.selectedTile:
            self.selectedTile.x = self.mouseX
            self.selectedTile.y = self.mouseY

    # Clicked on a tile? -> drag & drop
    # TODO: make this not use radius code 'cause it's not a circle lol
    def testMouse(self):
        for t in tiles:
            distX = math.fabs(self.mouseX-t.x)
            distY = math.fabs(self.mouseY-t.y)
            dist = (distY*distY)+(distX*distX)
            if (dist < 47/2 * 47/2): # lol radius
                self.selectedTile = t
                return
        
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

            # Draw the drag & drop tiles
            for t in tiles:
                t.draw(screen)

            
            #DrawHelper.drawAspect(screen,self.tileImage1, 0.68,0.7)
            #DrawHelper.drawAspect(screen,self.tileImage2, 0.74,0.7)
            #DrawHelper.drawAspect(screen,self.tileImage3, 0.8,0.7)
            #DrawHelper.drawAspect(screen,self.tileImage4, 0.86,0.7)
            #DrawHelper.drawAspect(screen,self.tileImage5, 0.92,0.7)

           
            
