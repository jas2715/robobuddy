#!/usr/bin/python
import pygame
import TextureLoader
import DrawHelper
import os
from GameScreen import GameScreen
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
        self.screen = pygame.display.set_mode(self.screenSize, pygame.FULLSCREEN)
		
	# Windowed mode
        #self.screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        TextureLoader.screenSize = self.screenSize
        
	# Init drawing
	DrawHelper.init(self.screenSize[0], self.screenSize[1])
        self.gs = GameScreen()
		
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

            # Clear Display
            screen.fill((255, 255, 0))  # 255 for white
			
			# Draw an image 
            #DrawHelper.drawAspect(screen,self.robotImage, 0,0)
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
