def releaseInMainGrid(mouseX,mouseY,selectedTile,mainMethod,tiles):
    xCord = 0
    yCord = 0
    droppedXRatio = float((mouseX-600))/float(151)
    if(droppedXRatio < .33):
        xCord = 0
    elif(droppedXRatio < .66):
        xCord = 1
    elif(droppedXRatio < 1.0):
        xCord = 2
    droppedYRatio = float((mouseY-120))/float(151)
    if(droppedYRatio < .33):
        yCord = 0
    elif(droppedYRatio < .66):
        yCord = 1
    elif(droppedYRatio < 1.0):
        yCord = 2
    selectedTile.x = (600 + ((151/3)*xCord)+2)
    selectedTile.y = (120 + ((151/3)*yCord)+2)
    for t in tiles:
        if(t.grid == "main" and t.gridX == xCord and t.gridY == yCord and t != selectedTile):
            tiles.remove(t)
    selectedTile.gridX = int(xCord)
    selectedTile.gridY = int(yCord)
    selectedTile.grid = "main"
    mainMethod[int(xCord)][int(yCord)] = selectedTile.action
    return

def releaseInSecondaryGrid(mouseX,mouseY,selectedTile,secondaryMethod,tiles):
	xCord = 0
	yCord = 0
	droppedXRatio = float((mouseX-600))/float(151)
	if(droppedXRatio < .33):
		xCord = 0
	elif(droppedXRatio < .66):
		xCord = 1
	elif(droppedXRatio < 1.0):
		xCord = 2
	droppedYRatio = float((mouseY-300))/float(101)
	if(droppedYRatio < .50):
		yCord = 0
	elif(droppedYRatio < 1.0):
		yCord = 1
	selectedTile.x = (600 + ((151/3)*xCord)+2)
	selectedTile.y = (300 + ((101/2)*yCord)+2)
	for t in tiles:
		if(t.grid == "secondary" and t.gridX == xCord and t.gridY == yCord):
			tiles.remove(t)
	selectedTile.gridX = int(xCord)
	selectedTile.gridY = int(yCord)
	selectedTile.grid = "secondary"
	secondaryMethod[int(xCord)][int(yCord)] = selectedTile.action
	return