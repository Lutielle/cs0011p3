import random

class Nutrient:
    #hasMoved = False
    def __init__(self):
    #The initializer should set hasMoved to False.
        self.hasMoved = False

    def getMoved(self):
    #Should return the current value of hasMoved.
        return self.hasMoved

    def setMoved(self):
    #Should set hasMoved to True.
        self.hasMoved = True

    def clearMoved(self):
    #Should set hasMoved to False
        self.hasMoved = False

class Microbe:
    #heldNutrient = None
    def __init__(self):
    #The initializer should an attribute named heldNutrient to None.
        self.heldNutrient = None

    def hasNutrient(self):
    #Should return True if the microbe has a nutrient, False otherwise.
        if self.heldNutrient != None:
            return True
        else:
            return False

    def takeNutrient(self, nutrient):
    #Should set assign the argument nutrient to heldNutrient.
        self.heldNutrient = nutrient

    def consumeNutrient(self):
    #Should set heldNutrient to None. This should be called whenever the nutrient reproduces.
        self.heldNutrient = None

class PetriCell:
    def __init__(self):
    #The initializer should set two attributes. microbe should be initialized to None and nutrients should be initialized to an empty list.
        self.microbe = None
        self.nutrients = []

    def getMicrobe(self):
    #Should return the value of the microbe attribute.
        return self.microbe

    def hasMicrobe(self):
    #Should return True if the microbe attribute is not None and False if it is None.
        if self.microbe != None:
            return True
        #elif microbe == None:
        else:
            return False

    def createMicrobe(self):
    #Should create a new Microbe object and assign it to the microbe attribute
        self.microbe = Microbe()

    def getNutrient(self):
    #Should remove a nutrient the from the nutrients attribute and return it. Should return None if nutrients is empty.
        if len(self.nutrients) == 0:
            return None
        else:
            return self.nutrients.pop()

    def getUnmoved(self):
    #Should remove all nutrients from nutrients that have hasMoved == False and return them in a list.
    #All nutrients with hasMoved == True should remain in nutrients.
        unmoved = []
        for nutrient in self.nutrients:
            if nutrient.getMoved() == False:
                self.nutrients.remove(nutrient)
                unmoved.append(nutrient)
        return unmoved

    def clearAllMoved(self):
    #Should call clearMoved() on each Nutrient object in nutrients.
        for nutrient in self.nutrients:
            nutrient.clearMoved()

    def hasNutrients(self):
    #Should return True if the nutrients attribute has any nutrients, and False if it is empty.
        if len(nutrients) == 0:
            return False
        else:
            return True

    def placeNutrient(self, nutrient):
    #Should add the argument nutrient to the attribute nutrients.
        self.nutrients.append(nutrient)

    def __str__(self):
    #Should give a string representation of the current cell. A cell with a microbe
    #and no nutrients should return "M0N". A cell with no microbe and 3 nutrients should return
    #"_3N". A cell with a microbe and 1 nutrient should return "M1N". Note that a nutrient held
    #by the microbe should not count towards the total. The format is “M” if there is a microbe,
    #“ ” if there is not, followed by the length of the nutrients attribute followed by an “N”.
        if self.microbe != None:
            print("M", end = "")
        else:
            print("_", end = "")

        print(len(self.nutrients), "N", sep = "")

"""class PetriDish:
    def __init__(self, x, y, concentration, microbes):
    x and y should be ints describing the size of the grid.
    You will represent the grid of a list of lists of PetriCell objects.
    You should store this list of lists in the attribute grid.
    grid[0][0] should represent the upper left corner of the grid, while
    grid[x - 1][y - 1] should represent the bottom right. This means that
    you should initialize grid as a list of x nested lists, each containing y PetriCell objects.
    Once you have created the grid, you should add nutrients and microbes. The concentration
    argument should be a float (between 0.0 and 1.0) specifying the percentage of the grid
    spaces that should contain a nutrient. Multiplying concentration, x, and y will tell you the
    number of nutrients to create (truncate the result to an int). You should randomly select
    valid indices (e.g., from 0 .. x - 1 and 0 .. y - 1) to place each of these nutrients. Use
    the random.randint function to select the index values. Note that this may place multiple
    nutrient objects initially in the same cell. This is fine.
    Finally, you should place the microbes. The microbes argument should be a list of tuples,
    where each tuple gives the coordinates where a microbe should be placed (e.g., [(75, 100), (125, 100)]
    would specify microbes to be placed at grid[75][100] and grid[125][100]).

    def moveNutrients(self):
    This method should move every nutrient in the grid once. For each
    nutrient, it should randomly choose to move the nutrient up, down, left, or right. For example,
    a nutrient in grid[5][5] could move to any of the following 8 options:
    – grid[4][4]
    – grid[4][5]
    – grid[4][6]
    – grid[5][4]
    – grid[5][6]
    – grid[6][4]
    – grid[6][5]
    – grid[6][6]
    Note that you must be careful not to move a nutrient “outside” of the grid. For example, a
    nutrient at grid[0][0] only has 3 possible options to move:
    – grid[0][1]
    – grid[1][0]
    – grid[1][1]
    After a nutrient is moved, set that nutrient’s hasMoved attribute to True to ensure it is not
    moved twice during this call to moveNutrients.
    In order to find all of the nutrients in the grid, you will need to iterate through each PetriCell
    object one at a time, and, for each PetriCell object, iterate through its unmoved nutrients.
    Once all nutrients have been moved, you should set all of their hasMoved attributes back to
    False so that they are ready for the next call to moveNutrients.
    • checkMicrobes(self): This method should check each microbe in the grid. For each microbe, it should first see if the microbe is not holding a nutrient, but there is a nutrient in that
    microbe’s PetriCell. If so, the method should remove that nutrient from the PetriCell and
    pass it to the microbe’s takeNutrient method. If, after that check, the microbe is holding a
    nutrient, it should attempt to reproduce. If the cell above, below, to the left, or to the right
    of the microbe does not have a microbe, the microbe should consume its held nutrient and the
    method should create a new microbe in that neighboring cell. The choice of creating a new
    microbe above, below, to the left, or to the right should be randomly for all valid cells (i.e.,
    cells without microbes). If all neighboring cells have microbes, the current microbe cannot
    reproduce.
    Note that you will not want to actually add the new microbe into the neighboring cell until
    all microbes have been checked to ensure that we do not create a microbe, and then have it
    reproduce in the same step. Use the following approach.
    1. Create a list of tuples representing all the microbes to created (as a list of tuples representing coordinates for new microbes).
    2. Every time a microbe would reproduce, add a new tuple to this list.
    3. Once all cells have been checked, create microbes at each coordinate specified in the list
    of tuples.
    • step(self, iterations): Should run through iterations steps of the simulation. Each
    step of the simulation should call moveNutrients() and then checkMicrobes().
    • __str__(self): This method will be essential for debugging. Should call __str__() for each
    PetriCell and return the result as a grid. Each row of the grid should be its own line. All
    of the cells in a row should be separated by a single space."""

class PetriDish:
    def __init__(self, x, y, concentration, microbes):
    """x and y should be ints describing the size of the grid.
    You will represent the grid of a list of lists of PetriCell objects.
    You should store this list of lists in the attribute grid.
    grid[0][0] should represent the upper left corner of the grid, while
    grid[x - 1][y - 1] should represent the bottom right. This means that
    you should initialize grid as a list of x nested lists, each containing y PetriCell objects."""
        self.grid = []
        for l in range(x):
            nested = []
            for i in range(y):
                nested.append(PetriCell())
            self.grid.append(nested)

    """Once you have created the grid, you should add nutrients and microbes. The concentration
    argument should be a float (between 0.0 and 1.0) specifying the percentage of the grid
    spaces that should contain a nutrient. Multiplying concentration, x, and y will tell you the
    number of nutrients to create (truncate the result to an int). You should randomly select
    valid indices (e.g., from 0 .. x - 1 and 0 .. y - 1) to place each of these nutrients. Use
    the random.randint function to select the index values. Note that this may place multiple
    nutrient objects initially in the same cell. This is fine."""
        #concentration is a float
        nutCount = int(concentration * x * y) #number of nutrients to place
        for nut in range(nutCount):
            xIndex = random.randint(0, x - 1)
            yIndex = random.randint(0, y - 1)
            #Both of these are negative 1 because list indexing starts at 0, of course
            self.grid[xIndex][yIndex].placeNutrient(Nutrient())

    """Finally, you should place the microbes. The microbes argument should be a list of tuples,
    where each tuple gives the coordinates where a microbe should be placed (e.g., [(75, 100), (125, 100)]
    would specify microbes to be placed at grid[75][100] and grid[125][100])."""
        for mic in microbes: #for tuple in list
            self.grid[mic[0]][mic[1]].createMicrobe()
            #place microbe at grid index [first item in tuple] [second item in tuple]

    def moveNutrients(self):
    """This method should move every nutrient in the grid once. For each
    nutrient, it should randomly choose to move the nutrient up, down, left, or right.
    For example, a nutrient in grid[5][5] could move to any of the following 8 options:
    – grid[4][4]
    – grid[4][5]
    – grid[4][6]
    – grid[5][4]
    – grid[5][6]
    – grid[6][4]
    – grid[6][5]
    – grid[6][6]
    Note that you must be careful not to move a nutrient “outside” of the grid. For example, a
    nutrient at grid[0][0] only has 3 possible options to move:
    – grid[0][1]
    – grid[1][0]
    – grid[1][1]
    After a nutrient is moved, set that nutrient’s hasMoved attribute to True to ensure it is not
    moved twice during this call to moveNutrients.
    In order to find all of the nutrients in the grid, you will need to iterate through each PetriCell
    object one at a time, and, for each PetriCell object, iterate through its unmoved nutrients.
    Once all nutrients have been moved, you should set all of their hasMoved attributes back to
    False so that they are ready for the next call to moveNutrients."""
        #for row in self.grid: -- I realized that I needed to fetch index values in order
            #for cell in row: -- to be able to move the nutrient, so these lines got rewritten.
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                cell = self.grid[row][col]
                #while cell.hasNutrients(): -- Also realized I wasn't checking if nutrients
                #had been moved already before moving them, so this was rewritten.
                unmoved = cell.getUnmoved()
                for nut in unmoved:
                    #welcome to the if block clusterfuck of making things not move off-grid
                    #I am not looking forward to doing this again with the microbes
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
    """This method should check each microbe in the grid. For each microbe, it should
    first see if the microbe is not holding a nutrient, but there is a nutrient in that
    microbe’s PetriCell. If so, the method should remove that nutrient from the PetriCell and
    pass it to the microbe’s takeNutrient method.

    If, after that check, the microbe is holding a nutrient, it should attempt to reproduce.
    If the cell above, below, to the left, or to the right of the microbe does not have a microbe,
    the microbe should consume its held nutrient and the method should create a new
    microbe in that neighboring cell. The choice of creating a new microbe above,
    below, to the left, or to the right should be randomly for all valid cells (i.e., cells without
    microbes). If all neighboring cells have microbes, the current microbe cannot reproduce.

    Note that you will not want to actually add the new microbe into the neighboring cell until
    all microbes have been checked to ensure that we do not create a microbe, and then have it
    reproduce in the same step. Use the following approach.
        1. Create a list of tuples representing all the microbes to created (as a list of tuples representing coordinates for new microbes).
        2. Every time a microbe would reproduce, add a new tuple to this list.
        3. Once all cells have been checked, create microbes at each coordinate specified in the list of tuples."""
        newMicrobes = []
        #this list will contain the tuple coordinates for the reproduced microbes

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
                else:
                    print(__str__(cell), end = " ")
