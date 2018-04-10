# DietPlanner

DietPlanner is a program to calculate the cheapest possible diet given a set of dietary constraints (the RDA dietary guidelines). It reads information about food prices and nutritive value from a csv file (‘foods.csv’, in res), sets up a linear programming problem, and solves it using PuLP. Results are printed to the screen and written to a file called HealthyDiet.lp

The program can be run from the command line. A file name can be specified as a command line argument for the program to read food data from, otherwise it will default to foods.csv. The input file must be a csv and follow the same format as foods.csv.

The program output (shown in HealthyDiet.lp) consists of the title of the diet (“Cheapest Healthy Diet”) followed by the type of LP problem being solved (in this case, a minimization problem) and then a set of equations. The first, ‘OBJ’, is the objective function being minimized. It consists of the food variables and their prices as their weights. Food variables are in units of pounds.

The problem constraints follow, with each representing a constraint presented by the RDA guidelines. For example, the first constraint specifies that the total caloric content of the food must add up to exactly 2000 (calories), while the fifth constraint (C5) says the total vitamin-A content must be at minimum 700 (micrograms).

The final section of test shows the status of the run (‘Optimal’ if a solution to the constraints was found) and the weight in pounds of each food which must be consumed every day to meet the dietary guidelines and minimize cost. For the foods listed in foods.csv, the cost per day is $2.93.

Data for food prices was taken from the Bureau of Labor Statistics Average Retail Food prices data, from Feb. 2018: https://www.bls.gov/regions/mid-atlantic/data/AverageRetailFoodAndEnergyPrices_USandMidwest_Table.htm

Nutritional information was found with WolframAlpha.

