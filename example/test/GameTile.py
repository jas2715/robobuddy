import pygame
import TextureLoader
import DrawHelper

class GameTile:
    def __init__(self, image, x, y, action):
        self.image = image
        self.x = x
        self.y = y
        self.action = action
        self.gridX = None
        self.gridY = None
        self.grid = None

    def move(self, x, y, TILEWIDTH):
        self.x = (x-TILEWIDTH/2)
        self.y = (y-TILEWIDTH/2)

    def draw(self, screen):
        DrawHelper.drawCoor(screen,self.image,self.x,self.y)
