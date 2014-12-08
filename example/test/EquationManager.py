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
    def __init__(self, val, boardX, boardY, screenX, screenY):
        self.value = val
        self.font = pygame.font.SysFont('ActionIsShaded', 24)
        self.label = self.font.render(str(self.value), 1, (10,10,10))
        self.pos = self.label.get_rect()
        self.pos.centerx = screenX
        self.pos.centery = screenY
        self.x = boardX
        self.y = boardY
        self.visible = True        

    def draw(self, screen):
        if self.visible:
            screen.blit(self.label, self.pos)

# Manages all possible game levels
class EquationManager:
    def __init__(self, rows, cols):
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
        self.op1 = "__"
        self.op2 = "__"

        # Fill the self.equations array
        self.equations = []
        self.makeEquations()
        self.eqIndex = None

        # The board, as represented by operands
        self.board = [[0 for x in range(rows)] for x in range(cols)] 
        
    # Helper functions to convert grid coordinates to screen coordinates
    def boardToScreenX(self, x):
        return self.boardX + (x+1) * self.tileWidth - self.tileWidth/2 - self.fontOffset
    def boardToScreenY(self, y):
        return self.boardY + (y+1) * self.tileWidth - self.tileWidth/2

    # Find anything on the board?
    def checkBoardContents(self, x, y):
        cell = self.board[x][y]
        if isinstance(cell, Operand):
            cell.visible = False
            if self.op1 == "__":
                self.op1 = str(cell.value)
                self.refresh_equation()
            elif self.op2 == "__":
                self.op2 = str(cell.value)
                self.refresh_equation()

    # Change equation
    def change_equation(self):
        # Randomize an equation to pick from 
        self.eqIndex = random.randrange(0, len(self.equations))
        self.refresh_equation()

        # Set the board contents
        rows = len(self.board)
        cols = len(self.board[0])
        self.board = [[0 for x in range(rows)] for x in range(cols)] 
        for item in self.equations[self.eqIndex].board_items:
            self.board[item.x][item.y] = item

    # Set all ops back to blank spaces and display the board contents
    # Call when re-running program
    def display_default(self):
        for item in self.equations[self.eqIndex].board_items:
            item.visible = True
        self.op1 = "__"
        self.op2 = "__"
        self.refresh_equation()

    # Update equation label with info
    def refresh_equation(self):
        self.equation_str = self.op1 + " " + self.equations[self.eqIndex].operator + " " + self.op2 + " = " + str(self.equations[self.eqIndex].answer)
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
            Operand(5, 1,1 ,self.boardToScreenX(1), self.boardToScreenY(1)),
            Operand(6, 2,2, self.boardToScreenX(2), self.boardToScreenY(2)),
            Operand(7, 3,3, self.boardToScreenX(3), self.boardToScreenY(3))
            ]))

        # 2: __+__= 9 (1,8,3)
        self.equations.append(Equation(9, "+", [
            Operand(1, 5,4, self.boardToScreenX(5), self.boardToScreenY(4)),
            Operand(8, 3,6, self.boardToScreenX(3), self.boardToScreenY(6)),
            Operand(3, 1,2, self.boardToScreenX(1), self.boardToScreenY(2))
            ]))
