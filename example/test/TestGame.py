#!/usr/bin/python
import pygame
import math
#from gi.repository import Gtk

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx = 10
        self.vy = -10
        self.radius = 50
        self.ballClicked = False
        self.mouseX = 0
        self.mouseY = 0

    def setPosition(self,x,y):
        self.x = x
        self.y = y

    def testCollision(self):
        distX = math.fabs(self.mouseX-self.x)
        distY = math.fabs(self.mouseY-self.y)
        dist = (distY*distY)+(distX*distX)
        if (dist < self.radius*self.radius):
            self.ballClicked = True

    def move(self,screen):
        if(self.ballClicked):
            self.x = self.mouseX
            self.y = self.mouseY
        else:
            self.x += self.vx
            self.y += self.vy

            while self.x > screen.get_width():
                self.x -= 1
                if (self.vx > 0): self.vx *= -1

            while self.x < 0:
                self.x += 1
                if (self.vx < 0): self.vx *= -1

            while self.y > screen.get_height():
                self.y -= 1
                if (self.vy > 0): self.vy *= -1

            while self.y < 0:
                self.y += 1
                if (self.vy < 0): self.vy *= -1

    def switchDirection(self):
        self.vx *= -1

class TestGame:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

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
        ball = Ball()
        screen = pygame.display.get_surface()
        mousePressed = False

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
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    ball.testCollision()
                elif event.type == pygame.MOUSEBUTTONUP :
                    ball.ballClicked = False
                elif event.type == pygame.MOUSEMOTION :
                    ball.mouseX,ball.mouseY = pygame.mouse.get_pos()

            # Move the ball
            ball.move(screen)

            # Clear Display
            screen.fill((255, 255, 0))  # 255 for white

            # Draw the ball
            pygame.draw.circle(screen, (0, 255, 0), (ball.x, ball.y), ball.radius)

            # Flip Display
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(30)


# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = TestGame()
    game.run()

if __name__ == '__main__':
    main()
