import random
from nmclass import Nutrient
from nmclass import Microbe

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
                #self.nutrients.remove(nutrient)
                #I realized this was messing up the loop by changing its indexing
                unmoved.append(nutrient)

        self.nutrients = list(set(self.nutrients) - set(unmoved))
        #so I opted to use sets to alter self.nutrients instead
        return unmoved

    def clearAllMoved(self):
    #Should call clearMoved() on each Nutrient object in nutrients.
        for nutrient in self.nutrients:
            nutrient.clearMoved()

    def hasNutrients(self):
    #Should return True if the nutrients attribute has any nutrients, and False if it is empty.
        if len(self.nutrients) == 0:
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
            #print("M", end = "")
            return "M{nutrients}N".format(nutrients = len(self.nutrients))
        else:
            #print("_", end = "")
            return "_{nutrients}N".format(nutrients = len(self.nutrients))

        #print(len(self.nutrients), "N", sep = "")
