import pygame
import TextureLoader
import DrawHelper

class MovingBot:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self, screen):
        DrawHelper.drawCoor(screen,self.image,self.x,self.y)
