import os
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")