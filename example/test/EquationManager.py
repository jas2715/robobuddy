import pygame
import TextureLoader
import DrawHelper
import random

# Represents an equation and its possible operands
class Equation:
    # Initialize with answer, operator, and a list of board items
    def __init__(self, ans, op, items):
        self.answer = ans
        self.operator = op
        self.board_items = items

# Number on the board to collect
class Operand:
    # Initialize value, position, and label/font
    def __init__(self, val, x, y):
        self.value = val
        self.font = pygame.font.SysFont('ActionIsShaded', 24)
        self.label = self.font.render(str(self.value), 1, (10,10,10))
        self.pos = self.label.get_rect()
        self.pos.centerx = x
        self.pos.centery = y

    def draw(self, screen):
        screen.blit(self.label, self.pos)

# Manages all possible game levels
class EquationManager:
    def __init__(self):
        # Positioning values
        self.boardX = 91
        self.boardY = 100
        self.tileWidth = 50
        self.fontOffset = 7 #(this one is guess-and-check)

        # Two sizes of the same font to use
        self.titleFont =  pygame.font.SysFont('ActionIsShaded', 48)
        self.labelFont = pygame.font.SysFont('ActionIsShaded', 24)

        # Data holders for displaying equation
        self.equation_str = ""
        self.equation_label = None
        self.equation_pos = None

        # Fill the self.equations array
        self.equations = []
        self.makeEquations()
        self.eqIndex = None
        
    # Helper functions to convert grid coordinates to screen coordinates
    def boardToScreenX(self, x):
        return self.boardX + x * self.tileWidth - self.tileWidth/2 - self.fontOffset
    def boardToScreenY(self, y):
        return self.boardY + y * self.tileWidth - self.tileWidth/2

    # Change equation
    def change_equation(self):
        # Randomize an equation to pick from 
        self.eqIndex = random.randrange(0, len(self.equations))

        # Update equation label
        self.equation_str = "__ " + self.equations[self.eqIndex].operator + " __" + " = " + str(self.equations[self.eqIndex].answer)
        self.equation_label = self.titleFont.render(self.equation_str, 1, (10,10,10))
        self.equation_pos = self.equation_label.get_rect()
        self.equation_pos.centerx = 200
        self.equation_pos.centery= 50

    # Draw screen elements
    def draw(self, screen):
        # Equation with or without blanks
        screen.blit(self.equation_label, self.equation_pos)

        # Operands on the board
        for item in self.equations[self.eqIndex].board_items:
            item.draw(screen)

    # Ugly hard-coded stuff that could be read in from a text file instead
    def makeEquations(self):
        # 1: __+__= 13 (5,6,7)
        self.equations.append(Equation(13, "+", [
            Operand(5, self.boardToScreenX(1), self.boardToScreenY(1)),
            Operand(6, self.boardToScreenX(2), self.boardToScreenY(2)),
            Operand(7, self.boardToScreenX(3), self.boardToScreenY(3))
            ]))

        # 2: __+__= 9 (1,8,3)
        self.equations.append(Equation(9, "+", [
            Operand(1, self.boardToScreenX(5), self.boardToScreenY(4)),
            Operand(8, self.boardToScreenX(3), self.boardToScreenY(6)),
            Operand(3, self.boardToScreenX(1), self.boardToScreenY(2))
            ]))
