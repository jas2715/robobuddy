import pygame
import TextureLoader
import DrawHelper

class MovingBot:
    def __init__(self, north, east, south, west, x, y, eqManager):
        self.north = north
        self.image = north
        self.east = east
        self.south = south
        self.west = west
        self.x = x
        self.y = y
        # 0 - north, 1 - east, 2 - south, 3 - west
        self.direction = 0
        self.xCoordinate = 4
        self.yCoordinate = 4
        # if the robot has moved at all from its original position it is no longer zeroed
        self.zeroed = True
        # Sorry this has to be here, but there's no way of tracking
        # the bot's movement step-by-step from the GameScreen class
        self.em = eqManager        

    # executes the passed in commands one by one
    def executeCommand(self,command):
        options = {
            'forward' : self.goForward,
            'turnleft' : self.turnLeft,
            'turnright' : self.turnRight,
            'grab' : self.grab,
        }
        # calls the correct function
        options[command]()
        self.updateDirection()
        self.zeroed = False

    def draw(self, screen):
        if(self.direction == 0):
            DrawHelper.drawCoor(screen,self.image,self.x,self.y) 
        elif(self.direction == 1):
            DrawHelper.drawCoor(screen,self.image,self.x-5,self.y+7)  
        elif(self.direction == 2):
            DrawHelper.drawCoor(screen,self.image,self.x,self.y+2)
        elif(self.direction == 3):
            DrawHelper.drawCoor(screen,self.image,self.x-7,self.y+7)
    def updateDirection(self):
        if(self.direction == 0):
            self.image = self.north
        elif(self.direction == 1):
            self.image = self.east
        elif(self.direction == 2):
            self.image = self.south
        elif(self.direction == 3):
            self.image = self.west       

    def goForward(self):
        if(self.direction == 0):
            self.y -= 50
            self.yCoordinate -= 1
        if(self.direction == 1):
            self.x += 50
            self.xCoordinate += 1
        if(self.direction == 2):
            self.y += 50
            self.yCoordinate += 1
        if(self.direction == 3):
            self.x -= 50
            self.xCoordinate -= 1

    def grab(self):
        # Did the bot find anything on the board?
        self.em.checkBoardContents(self.xCoordinate, self.yCoordinate)

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
        self.x = 291
        self.y = 300
        self.xCoordinate = 4
        self.yCoordinate = 4
        self.updateDirection()
        self.zeroed = True
