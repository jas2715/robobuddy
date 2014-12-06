import pygame

def executeCommands(self):
    if self.botRunning:
        #if Robobuddy has not reached the end of his commands
        if len(self.commands) > self.currentCommand:
            # get the current command 
            cmd = self.commands[self.currentCommand]
            # if that command is to grab a number then grab the number Robobuddy is standing on
            if(cmd == "grab"):
                pygame.time.delay(400)
                print("Grab")
                # increment current command since it's done now
                self.currentCommand += 1
            # if the current command is actually to run the function then we go into a second loop
            elif(cmd == "function"):
                if (len(self.secondaryCommands) > self.currentSecondaryCommand):
                    #runs step by step through the functions commands (exactly like in the above main method loop)
                    cmd2 = self.secondaryCommands[self.currentSecondaryCommand]
                    #Recursion by returning to beginning of this loop
                    if(cmd2 == "function"):
                        self.currentSecondaryCommand = 0
                    #if the command is to grab a number then grab the number Robobuddy is standing on
                    if(cmd2 == "grab"):
                        pygame.time.delay(400)
                        print("Grab")
                        # Same as before but now increment currentSECONDARYcommand since were in the function
                        self.currentSecondaryCommand += 1
                    #if the command is to turn or move then do so
                    elif(cmd2 == "turnleft" or cmd2 == "turnright" or cmd2 == "forward"):
                        #ensure the bot isn't going off the grid - only execute if the robot is safe to move
                        if(cmd2 == "forward"):
                            pygame.time.delay(400)
                            if(self.bot.direction == 0 and self.bot.yCoordinate != 0):
                                self.bot.executeCommand(cmd2)
                            elif(self.bot.direction == 1 and self.bot.xCoordinate != 8):
                                self.bot.executeCommand(cmd2)
                            elif(self.bot.direction == 2 and self.bot.yCoordinate != 8):
                                self.bot.executeCommand(cmd2)
                            elif(self.bot.direction == 3 and self.bot.xCoordinate != 0):
                                self.bot.executeCommand(cmd2)
                            #Increment commands regardless of if robot moved so that it isn't stuck against a wall
                            self.currentSecondaryCommand += 1
                        else:
                            pygame.time.delay(400)
                            self.bot.executeCommand(cmd2)
                            # Same as before but now increment currentSECONDARYcommand since were in the function
                            self.currentSecondaryCommand += 1
                #if the function is complete, increment the main list of commands, and reset the counter
                else:
                    self.currentCommand += 1
                    self.currentSecondaryCommand = 0
            #if the command is to turn or move then do so        
            elif(cmd == "turnleft" or cmd == "turnright" or cmd == "forward"):
                #ensure the bot isn't going off the grid - only execute if the robot is safe to move
                if(cmd == "forward"):
                    pygame.time.delay(400)
                    if(self.bot.direction == 0 and self.bot.yCoordinate != 0):
                        self.bot.executeCommand(cmd)
                    elif(self.bot.direction == 1 and self.bot.xCoordinate != 8):
                        self.bot.executeCommand(cmd)
                    elif(self.bot.direction == 2 and self.bot.yCoordinate != 8):
                        self.bot.executeCommand(cmd)
                    elif(self.bot.direction == 3 and self.bot.xCoordinate != 0):
                        self.bot.executeCommand(cmd)
                    #Increment commands regardless of if robot moved so that it isn't stuck against a wall
                    self.currentCommand += 1
                else:
                    pygame.time.delay(400)
                    self.bot.executeCommand(cmd)
                    self.currentCommand += 1
        # if robobuddy has reached the end of his commands then stop running and reset current command
        else:
            self.currentCommand = 0
            self.botRunning = False
            self.gameState = 0