import pygame
import TextureLoader
import DrawHelper
import random

equations = [
    #(answer, operator, (value, x, y), (value, x, y) )
    (16, "+", (9, 0, 0), (7, 1, 1), (8, 2, 2), (6, 3, 3) ),
    #(11, "+", (), (), (), () ),
    #(9, "-", (), (), (), () ),
    ]

class EquationManager:
    def __init__(self):
        self.eqIndex = None
        self.boardItems = []

        self.boardX = 91
        self.boardY = 100
        self.tileWidth = 50

        # Two sizes of the same font to use
        self.titleFont =  pygame.font.SysFont('ActionIsShaded', 48)
        self.labelFont = pygame.font.SysFont('ActionIsShaded', 24)


    # Change equation
    def change_equation(self):
        # Randomize an equation to pick from 
        self.eqIndex = random.randrange(0, len(equations))

        # Update everything based on the new equation
        for x in range(2, len(equations[self.eqIndex])):
            self.boardItems.append(equations[self.eqIndex][x])

    def draw(self, screen):
        # Draw the equation
        eq_str = "__" + "+" + "__" + "=" + str(equations[self.eqIndex][0])
        labelEq = self.titleFont.render(eq_str, 1, (10,10,10))
        eqPos = labelEq.get_rect()
        eqPos.centerx = 200
        eqPos.centery = 50
        screen.blit(labelEq, eqPos)
        
        # Draw the text onto the board
        for item in self.boardItems:   
            labelItem = self.labelFont.render(str(item[0]), 1, (10,10,10))
            eqPos = labelItem.get_rect()
            eqPos.centerx = self.boardX + item[1] * self.tileWidth + 20 
            eqPos.centery = self.boardY + item[2] * self.tileWidth + 25 
            screen.blit(labelItem, eqPos)
