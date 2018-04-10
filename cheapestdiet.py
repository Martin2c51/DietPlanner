#!/usr/bin/env python

"""
Author: Luke Gehman

This program uses linear programming techniques to determine the cheapest
possible diet given some set of dietary constraints.

"""

import csv
from pulp import *


class CheapestDiet(object):

    """
    Reads price and nutrition info on various food items from a file, and
    computes the cheapest possible diet with those food items which still
    meets certain nutritional goals.

        Attributes:
            filename: Name of the file to read from
            constraints: A dictionary of constraints the LP must satisfy
            food_items: A list of the food items available
            prices: A dictionary of the prices of the food items
            calorie_content: A dictionary of the caloric content of the food items
            sat_fat_content: A dictionary of the saturated fat content of the food items
            sodium_content: A dictionary of the sodium content of the food items
            vitamin_c_content: A dictionary of the vitamin C content of the food items
            vitamin_a_content: A dictionary of the vitamin A content of the food items
            protein_content: A dictionary of the protein content of the food items

    """

    def __init__(self, filename):
        """Sets constraints to the default, and reads food info from the indicated file"""
        self.filename = filename
        self.constraints = {}
        self.set_constraints()

        self.food_items = []
        self.prices = {}
        self.calorie_content = {}
        self.sat_fat_content = {}
        self.sodium_content = {}
        self.vitamin_c_content = {}
        self.vitamin_a_content = {}
        self.protein_content = {}
        self.read_foods_file()

    def calculate(self):
        """Sets up and solves a LP based on the information and constraints given"""

        # Set up the model with food items as variables
        diet_model = pulp.LpProblem("Cheapest Healthy Diet", pulp.LpMinimize)
        x = pulp.LpVariable.dict('x_%s', self.food_items, lowBound=0)

        # Objective function based on prices of the foods
        diet_model += sum([self.prices[i] * x[i] for i in self.food_items])

        # Dietary Constraints
        diet_model += sum([self.calorie_content[i] * x[i] for i in self.food_items]) == self.constraints['calories']
        diet_model += sum([self.sat_fat_content[i] * x[i] for i in self.food_items]) <= self.constraints['max_saturated_fat']
        diet_model += sum([self.sodium_content[i] * x[i] for i in self.food_items]) <= self.constraints['max_sodium']
        diet_model += sum([self.vitamin_c_content[i] * x[i] for i in self.food_items]) >= self.constraints['min_vitamin_c']
        diet_model += sum([self.vitamin_a_content[i] * x[i] for i in self.food_items]) >= self.constraints['min_vitamin_a']
        diet_model += sum([self.protein_content[i] * x[i] for i in self.food_items]) >= self.constraints['min_protein']

        # Solve the model and report the results
        diet_model.writeLP("HealthyDiet.lp")
        diet_model.solve()
        self.report_results(diet_model)

    def read_foods_file(self):
        """ Reads a csv file with food names, prices, and nutritional info (see foods.csv for formatting)"""
        with open(self.filename, 'r', newline='') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            self.food_items = next(reader)[1:]
            self.prices = dict(zip(self.food_items, next(reader)[1:]))
            self.calorie_content = dict(zip(self.food_items, next(reader)[1:]))
            self.sat_fat_content = dict(zip(self.food_items, next(reader)[1:]))
            self.sodium_content = dict(zip(self.food_items, next(reader)[1:]))
            self.vitamin_c_content = dict(zip(self.food_items, next(reader)[1:]))
            self.vitamin_a_content = dict(zip(self.food_items, next(reader)[1:]))
            self.protein_content = dict(zip(self.food_items, next(reader)[1:]))

    def set_constraints(self, calories=2000, fat_g=20, sodium_mg=2400,
                        vitamin_c_mg=90, vitamin_a_mcg=700, protein_g=56):
        """Sets the dietary constraints for the LP problem"""
        self.constraints['calories'] = calories  # calories
        self.constraints['max_saturated_fat'] = fat_g  # grams
        self.constraints['max_sodium'] = sodium_mg  # milligrams
        self.constraints['min_vitamin_c'] = vitamin_c_mg  # milligrams
        self.constraints['min_vitamin_a'] = vitamin_a_mcg  # micrograms
        self.constraints['min_protein'] = protein_g  # grams

    def report_results(self,diet_model):
        """ Prints the solution, and writes it to a file called HealthyDiet.lp"""
        file = open("HealthyDiet.lp", "a+")
        status = "\nStatus: " + LpStatus[diet_model.status] + '\n'
        file.write(status)
        print(status)
        for food in diet_model.variables():
            output = food.name + " = " + str(food.varValue) + " pounds\n"
            file.write(output)
            print(output)
        total_cost = "Cost/day = $" + str(format(value(diet_model.objective), '.2f'))
        file.write(total_cost)
        print(total_cost)
        file.close()






