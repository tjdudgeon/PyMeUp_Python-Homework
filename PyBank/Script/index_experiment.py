import os
import csv

#Establishing file path to get to CSV
csvpath = os.path.join("..", "Resources", "budget_data.csv")

#Initializing variable
total_months = 0
total_profit_loss = 0
initial_avg_value = 0
total_change = []
dates = []
profits_losses = []


#Reading csv
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #Skip header row
    next(csv_reader, None)


    #Counting total number of months
    for months in csv_reader:
        total_months += 1

        #Counting net profit/loss
        total_profit_loss += int(months[1])

        #Updating "dates" and "profits_losses" lists to use for indexing
        dates.append(months[0])
        profits_losses.append(months[1])
        
        
print(dates)