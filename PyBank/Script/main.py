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

        #Gathering profit/loss changes between dates
        current_value = months[1]
        value_change = int(current_value) - int(initial_avg_value)
        total_change.append(value_change)
        initial_avg_value = current_value

    #Define function to calculate average change between dates
    def average(total_change):
        all_months = len(total_change)
        total = sum(total_change) - total_change[0]
        avg = total/(all_months - 1)
        return avg

    avg_change = round(average(total_change),2)

#Establish greatest increase and decrease values
greatest_increase = max(total_change)
greatest_decrease = min(total_change)
greatest_increase_index = total_change.index(greatest_increase)
greatest_decrease_index = total_change.index(greatest_decrease)
greatest_increase_month = dates[greatest_increase_index]
greatest_decrease_month = dates[greatest_decrease_index]
        
##Check to see if calculations are correct
# print(total_months)
# print(f"$" + str(total_profit_loss))
# print(avg_change)
# print(f"$" + str(greatest_increase))
# print(f"$" + str(greatest_decrease))
# print(greatest_increase_month)
# print(greatest_decrease_month)

#Print financial analysis
print("Financial Analysis")
print("----------------------------------------------------------------")
print(f"Total Months: " + str(total_months))
print(f"Net Total: " + "$" + str(total_profit_loss))
print(f"Average Change in Profits: " + "$" + str(avg_change))
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Increase in Profits:  {greatest_decrease_month} (${greatest_decrease})")

#Specifying file to write to
analysis_file = os.path.join("..", "Analysis", "analysis_results.txt") 

#Open the file using "write mode"
with open(analysis_file, "w") as writer:
    writer.write("Financial Analysis\n")
    writer.write("-------------------------\n")
    writer.write(f"Total Months: {total_months}\n")
    writer.write(f"Net Total: ${total_profit_loss}\n")
    writer.write(f"Average Change in Profits: ${avg_change}\n")
    writer.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    writer.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")