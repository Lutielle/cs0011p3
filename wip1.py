class Nutrient:
    #hasMoved = False
    def __init__(self):
    #The initializer should set hasMoved to False.
        hasMoved = False
    def getMoved(self):
    #Should return the current value of hasMoved.
        return hasMoved
    def setMoved(self):
    #Should set hasMoved to True.
        hasMoved = True
    def clearMoved(self):
    #Should set hasMoved to False
        hasMoved = False

class Microbe:
    #heldNutrient = None
    def __init__(self):
    #The initializer should an attribute named heldNutrient to None.
        heldNutrient = None
    def hasNutrient(self):
    #Should return True if the microbe has a nutrient, False otherwise.
        if heldNutrient != None:
            return True
        else:
            return False
    def takeNutrient(self, nutrient):
    #Should set assign the argument nutrient to heldNutrient.
        nutrient = heldNutrient
    def consumeNutrient(self):
    #Should set heldNutrient to None. This should be called whenever the nutrient reproduces.
        heldNutrient = None

class PetriCell:
    def __init__(self):
    #The initializer should set two attributes. microbe should be initialized to None and nutrients should be initialized to an empty list.
        microbe = None
    getMicrobe(self):
    #Should return the value of the microbe attribute.
    hasMicrobe(self):
    #Should return True if the microbe attribute is not None and False if it is None.
    createMicrobe(self):
    #Should create a new Microbe object and assign it to the microbe attribute
    getNutrient(self):
    #Should remove a nutrient the from the nutrients attribute and return it. Should return None if nutrients is empty.
    getUnmoved(self):
    #Should remove all nutrients from nutrients that have hasMoved == False and return them in a list.
    #All nutrients with hasMoved == True should remain in nutrients.
    clearAllMoved(self):
    #Should call clearMoved() on each Nutrient object in nutrients.
    hasNutrients(self):
    #Should return True if the nutrients attribute has any nutrients, and False if it is empty.
    placeNutrient(self, nutrient):
    #Should add the argument nutrient to the attribute nutrients.
    __str__(self):
    #Should give a string representation of the current cell. A cell with a microbe
    #and no nutrients should return "M0N". A cell with no microbe and 3 nutrients should return
    #"_3N". A cell with a microbe and 1 nutrient should return "M1N". Note that a nutrient held
    #by the microbe should not count towards the total. The format is “M” if there is a microbe,
    #“ ” if there is not, followed by the length of the nutrients attribute followed by an “N”.

class PetriDish:
    pass
