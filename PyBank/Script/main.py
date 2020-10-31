import os
import csv

#Establishing file path to get to CSV
csvpath = os.path.join("..", "Resources", "budget_data.csv")

#Initializing variable
total_months = 0


#Reading csv
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #Skip header row
    next(csv_reader, None)

    #Counting total number of months
    for months in csv_reader:
        total_months += 1

    print(total_months)
        
 