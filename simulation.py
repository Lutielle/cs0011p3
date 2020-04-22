import random
from nmclass import Nutrient
from nmclass import Microbe
from petricell import PetriCell
from petridish import PetriDish

def main():
    test_grid = PetriDish(10, 10, .25, [(4,4)])
    #test_grid = PetriDish(200, 200, .3, [(75,100), (125, 100)])

    test_grid.step(10)

main()
