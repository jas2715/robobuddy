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

        self.x = -100
        self.y = 100

        self.vx = 10
        self.vy = 0
        
		# Do a test draw
        #self.robotImage = TextureLoader.load(os.path.join('assets', 'bot-sketch.png'), (89,106))
        #DrawHelper.drawAspect(self.screen,self.robotImage, 0,0)
        self.gs = GameScreen()
		
        self.paused = False
        self.direction = 1

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
            #    Gtk.main_iteration()

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.direction = -1
                    elif event.key == pygame.K_RIGHT:
                        self.direction = 1

            # Move the ball
            if not self.paused:
                self.x += self.vx * self.direction
                if self.direction == 1 and self.x > screen.get_width() + 100:
                    self.x = -100
                elif self.direction == -1 and self.x < -100:
                    self.x = screen.get_width() + 100

                self.y += self.vy
                if self.y > screen.get_height() - 100:
                    self.y = screen.get_height() - 100
                    self.vy = -self.vy

                self.vy += 5

            # Clear Display
            screen.fill((255, 255, 0))  # 255 for white

            # Draw the ball
            pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), 100)
			
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
