import pygame
import TextureLoader
import DrawHelper

class MovingBot:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        # 0 - north, 1 - east, 2 - south, 3 - west
        self.direction = 0

    # executes the passed in commands one by one
    def executeCommand(self,command):
        options = {
            'forward' : self.goForward,
            'turnleft' : self.turnLeft,
            'turnright' : self.turnRight,
        }
        # calls the correct function
        options[command]()

    def draw(self, screen):
        DrawHelper.drawCoor(screen,self.image,self.x,self.y)

    def goForward(self):
        if(self.direction == 0):
            self.y -= 50
        if(self.direction == 1):
            self.x += 50
        if(self.direction == 2):
            self.y += 50
        if(self.direction == 3):
            self.x -= 50

    def turnLeft(self):
        self.direction -= 1
        if(self.direction < 0):
            self.direction = 3

    def turnRight(self):
        self.direction += 1
        if(self.direction > 3):
            self.direction = 0

    def reset(self):
        self.direction = 0
        self.x = 91
        self.y = 100
