import pygame
import TextureLoader
import DrawHelper
import os

class MenuScreen:
    # Load all of the textures, fonts, titles, etc.
    def __init__(self):
        self.clicked = False

        # Images
        self.playButton = TextureLoader.load(os.path.join('assets', 'button-start.png'), (154,67))
        self.background = TextureLoader.load(os.path.join('assets', 'menu.png'), (800,600))

        # Two sizes of the same font to use
        self.titleFont =  pygame.font.SysFont('ActionIsShaded', 96)
        self.labelFont = pygame.font.SysFont('ActionIsShaded', 48)

    def pressMouse(self):

        print("Mouse pressed")
        print(self.mouseX)
        print(self.mouseY)
        
        # Is the user clicking on the Go button?
        tempX = 65
        tempY = 250
        if(self.mouseX > tempX) and (self.mouseX < tempX + 154) and (self.mouseY > tempY) and (self.mouseY < tempY + 67):
            self.clicked = True

    # Draw all screen elements here!
    def draw(self, screen):
    	if screen != 0:
            # Background image
            DrawHelper.drawCoor(screen,self.background,0,0)
            
             # Text blocks
            title1 = self.titleFont.render("Robobuddy", 1, (10,10,10))
            title1pos = title1.get_rect()
            title1pos.centerx = 250
            title1pos.centery = 150
            screen.blit(title1, title1pos)

            # Buttons
            DrawHelper.drawCoor(screen,self.playButton,65,250)
