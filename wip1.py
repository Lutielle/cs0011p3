class Nutrient:
    hasMoved = False

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
    heldNutrient = None

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
    pass

class PetriDish:
    pass
