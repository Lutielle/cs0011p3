import random

class Nutrient:
    #hasMoved = False
    def __init__(self):
        """The initializer should set hasMoved to False."""
        self.hasMoved = False

    def getMoved(self):
        """Should return the current value of hasMoved."""
        return self.hasMoved

    def setMoved(self):
        """Should set hasMoved to True."""
        self.hasMoved = True

    def clearMoved(self):
        """Should set hasMoved to False."""
        self.hasMoved = False

class Microbe:
    #heldNutrient = None
    def __init__(self):
        """The initializer should an attribute named heldNutrient to None."""
        self.heldNutrient = None

    def hasNutrient(self):
        """Should return True if the microbe has a nutrient, False otherwise."""
        return self.heldNutrient is not None

    def takeNutrient(self, nutrient):
        """Should set assign the argument nutrient to heldNutrient."""
        self.heldNutrient = nutrient

    def consumeNutrient(self):
        """Should set heldNutrient to None. This should be called whenever the
        nutrient reproduces."""
        self.heldNutrient = None
