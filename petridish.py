import random
import nmclass
import petricell

class PetriDish:
    def __init__(self, x, y, concentration, microbes):
    #x and y should be ints describing the size of the grid
        self.grid = []
        for l in range(x):
            nested = []
            for i in range(y):
                nested.append(PetriCell())
            self.grid.append(nested)

    #Add a number of nutrients (int) based on concentration (float)
        nutCount = int(concentration * x * y) #number of nutrients to place
        for nut in range(nutCount):
            xIndex = random.randint(0, x - 1)
            yIndex = random.randint(0, y - 1)
            #Both of these are - 1 to accomodate list indexing starting at 0
            self.grid[xIndex][yIndex].placeNutrient(Nutrient())

    #Place microbes; the microbes argument should be a list of tuples specifying coordinates
        for mic in microbes: #for tuple in list
            self.grid[mic[0]][mic[1]].createMicrobe()
            #place microbe at grid index [first item in tuple] [second item in tuple]

    def moveNutrients(self):
    #Move each nutrient in the grid once to any of the 8 surrounding spaces,
    #then set its hasMoved attribute to True
    #Once all nutrients have moved, set hasMoved back to False

        #for row in self.grid: -- I realized that I needed to fetch index values in order
            #for cell in row: -- to be able to move the nutrient, so these lines got rewritten.
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                cell = self.grid[row][col]
                #while cell.hasNutrients(): -- Also realized I wasn't checking if nutrients
                #had been moved already before moving them, so this was rewritten.
                unmoved = cell.getUnmoved()
                for nut in unmoved:
                    #welcome to the nightmare if block of making things not move off-grid
                    #I am not looking forward to potentially doing this again with the microbes
                    if row == 0:
                        xMove = random.randint(0, 1)
                        #generates 0 or 1 to prevent moving off-grid
                    elif row == len(self.grid) - 1:
                        xMove = random.randint(-1, 0)
                        #generates -1 or 0 to prevent moving off-grid
                    else:
                        xMove = random.randint(-1, 1)
                        #generates -1, 0, or 1

                    if col == 0 and xMove == 0:
                        yMove = 1
                        #yMove = -1 moves off-grid; yMove = 0 results in no movement
                    elif col == 0:
                        yMove = random.randint(0, 1)
                        #generates 0 or 1 to prevent moving off-grid
                    elif col == len(self.grid[row]) - 1 and xMove == 0:
                        yMove = -1
                        #yMove = 1 moves off-grid; yMove = 0 results in no movement
                    elif col == len(self.grid[row]) - 1:
                        yMove = random.randint(-1, 0)
                        #generates -1 or 0 to prevent moving off-grid
                    elif xMove == 0:
                        yMove = random.randrange(-1, 2, 2)
                        #generates -1 or 1 to prevent no movement
                    else:
                        yMove = random.randint(-1, 1)
                        #generates -1, 0, or 1

                    #It is at this point it occurred to me that I think I'm using x and y
                    #backwards of their mathematical meanings here, since row should
                    #associate with the y coordinate and column with the x coordinate.
                    #But rewriting and potentially breaking my code to appease math sounds not worth.
                    #(My mathematician girlfriend gave me her blessing, so it's staying backwards.)
                    row = row + xMove
                    col = col + yMove

                    self.grid[row][col].placeNutrient(nut)
                    nut.setMoved()

        for row in self.grid:
            for cell in row:
                if cell.hasNutrients() != False:
                    cell.clearAllMoved()

    def checkMicrobes(self):
    #Check each microbe in the grid:
    #If it is not holding a nutrient, but there is one in the cell,
    #it should take that nutrient, then attempt to reproduce.
    #To do this, check that there is a valid neighboring cell (one that does not contain a microbe).
    #Then, of the valid neighbors, select one at random.
    #If there are none, the microbe does not reproduce.
        newMicrobes = []
        #this list will contain the tuple coordinates for the microbes to be reproduced

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                cell = self.grid[row][col]
                #I Need Index Values 2: Electric Boogaloo
                if cell.hasMicrobe() != False:
                    #if the cell contains a microbe
                    mic = cell.getMicrobe()
                    #making a Microbe object to act on
                    if mic.hasNutrient() == False and cell.hasNutrients() == True:
                    #if the microbe doesn't have a nutrient and the cell does
                        mic.takeNutrient(getNutrient())
                        #make heldNutrient True and remove the nutrient from that cell's nutrients list

                        #Welcome to the neighbor-testing section!
                        validNeighbors = []
                        #the plan is the make a list of tuple coordinates for valid neighbors
                        #and then randomly select one from the list using random
                        #if mic.hasNutrient() == True: -- Implied already.
                        for xNeighbor in range(-1, 2):
                            for yNeighbor in range(-1, 2):
                                neighbor = self.grid[xNeighbor][yNeighbor]
                                #Index Values: Return of the - you know, this is way less funny.
                                if xNeighbor == 0:
                                    if yNeighbor == 0:
                                    #excluding the original cell
                                        continue
                                if neighbor.hasMicrobe() == False:
                                #testing whether neighbors have microbes
                                    validNeighbors.append((xNeighbor, yNeighbor))
                                    #and if they don't, add their coordinates to a list

                        try:
                            newMicrobes.append(random.choice(validNeighbors))
                            #randomly select a valid neighbor and add it to the new microbe list
                        except IndexError:
                            pass
                            #and if there are no valid neighbors, don't error out

                        mic.consumeNutrient()
                        #set the microbe's heldNutrient to False again

        for coord in newMicrobes: #for tuple in list
            self.grid[mic[0]][mic[1]].createMicrobe() #make a new microbe

    def step(self, iterations):
    #Should run through iterations steps of the simulation.
    #Each step of the simulation should call moveNutrients() and then checkMicrobes().
        for i in range(interations + 1):
            self.moveNutrients()
            self.checkMicrobes()

    def __str__(self):
    #This method will be essential for debugging. Should call __str__() for each
    #PetriCell and return the result as a grid. Each row of the grid should be its own line. All
    #of the cells in a row should be separated by a single space.
        for row in self.grid:
            for cell in row:
                if cell = row[-1]:
                    print(__str__(cell))
                print(__str__(cell), end = " ")
