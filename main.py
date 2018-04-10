#!/usr/bin/env python

"""
Author: Luke Gehman

This program uses linear programming techniques to determine the cheapest
possible diet given some set of dietary constraints.

"""

import sys
import cheapestdiet as diet


def main():
    """ Calculates a cheapest diet from a file name passed through command line
        Prints the results, and writes them to a txt file in same directory"""

    if len(sys.argv) > 1:
        diet_test = diet.CheapestDiet(sys.argv[1])
    else:
        diet_test = diet.CheapestDiet("res/foods.csv")

    diet_test.calculate()
    print("Finished with success!")


main()
