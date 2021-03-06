#!/usr/bin/python
import pygame
import TextureLoader
import DrawHelper
import os
from GameScreen import GameScreen
from MenuScreen import MenuScreen
#from gi.repository import Gtk

class TestGame:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()
		
        # Full screen mode
        width = pygame.display.Info().current_w
        height = pygame.display.Info().current_h
        if(float(width)/float(height) == float(4)/float(3)):
            self.screenSize = (width,height)
        else:
		self.screenSize = (800,600)
        self.screen = pygame.display.set_mode(self.screenSize, pygame.RESIZABLE)
		
	# Windowed mode
        #self.screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        TextureLoader.screenSize = self.screenSize

        # 0 = Menu, 1 = Game
        self.gameState = 0
        
	# Init values
	DrawHelper.init(self.screenSize[0], self.screenSize[1])
        self.gs = GameScreen()
        self.ms = MenuScreen()
        self.font =  pygame.font.SysFont('ActionIsShaded', 12)
		
        self.paused = False

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    # The main game loop.
    def run(self):
        self.running = True

        screen = pygame.display.get_surface()

        while self.running:
            # Pump GTK messages.
            #while Gtk.events_pending():
            # Gtk.main_iteration()

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    if self.gameState == 0:
                        self.ms.pressMouse()
                    elif self.gameState == 1:
                        self.gs.pressMouse()                    
                elif event.type == pygame.MOUSEBUTTONUP :
                    self.gs.releaseMouse()
                    self.gs.selectedTile = None
                elif event.type == pygame.MOUSEMOTION :
                    if self.gameState == 0:
                        self.ms.mouseX,self.ms.mouseY = pygame.mouse.get_pos()
                    elif self.gameState == 1:
                        self.gs.mouseX,self.gs.mouseY = pygame.mouse.get_pos()

            # Clear Display
            screen.fill((255, 255, 0))  # 255 for white

            # Game or menu?
            if self.gameState == 0:
                # Menu draw
                self.ms.draw(self.screen)
                if self.ms.clicked:
                    self.gameState = 1
                    self.ms.clicked = False
            elif self.gameState == 1:
                # Game loop, then draw
                self.gs.update()
                self.gs.draw(self.screen)

            # Flip Display
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(30)


# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    #pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = TestGame()
    game.run()

if __name__ == '__main__':
    main()
