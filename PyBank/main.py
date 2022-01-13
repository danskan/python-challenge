import csv
import os

# Read the file and store to variable
csvpath = os.path.join('Resources', 'budget_data.csv')
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    data = list(csvreader)

#Sum the total profit and losses
def get_total(data):
    total = 0
    for amount in data[1:]:
        amount = int(amount[1])
        total += amount
    return total

# Count months
def count_months(data):
    months = 0
    for month in data[1:]:
        months += 1
    return months

# Get Average Profit Per Month
def average_profit(gross_profit, number_of_months):
    return round(gross_profit/number_of_months,2)

# Report Best Month
def best_month(data):
    highest_profit = 0
    top_month = ''
    for amount in data[1:]:
        if int(amount[1]) > int(highest_profit):
            highest_profit = amount[1]
            top_month = amount[0]
    return highest_profit, top_month

# Report Worst Month
def worst_month(data):
    worst_loss = 0
    bottom_month = ''
    for amount in data[1:]:
        if int(amount[1]) < int(worst_loss):
            worst_loss = amount[1]
            bottom_month = amount[0]
    return worst_loss, bottom_month

# Find and count the negative profit months
def count_negative_profit_months(data):
    negative_months = 0
    for amount in data[1:]:
        if int(amount[1]) < 0:
            negative_months += 1
    return negative_months

# Calling the functions and storing outputs
gross_profit = get_total(data)
gross_profit_line = f"The Gross Annual Profit is $" + str(gross_profit)

number_of_months = (count_months(data))
number_of_months_line = f"Gross profit was earned over " + str(number_of_months) + " months"

mean_profit = average_profit(gross_profit, number_of_months)
mean_profit_line = f"The Average Price Per Month is $" + str(mean_profit)

highest_profit, top_month = best_month(data)
highest_profit_line = f"The Best Month on Record is " + str(top_month) + " had a profit of $" + str(highest_profit)

worst_loss, bottom_month = worst_month(data)
worst_loss_line = f"The Worst Month on Record is " + str(bottom_month) + " had a profit of $" + str(worst_loss)

loss_months = count_negative_profit_months(data)
loss_months_line = f"There were " + str(loss_months) + " months with negative profit"

# Printing to terminal
print("Financial Analysis")
print("-----------------------------------------")
print(gross_profit_line)
print(number_of_months_line)
print(mean_profit_line)
print(worst_loss_line)
print(loss_months_line)

# Output result to text file
output_title_line = "Financial Analysis"
border_line = "-----------------------------------------"
all_lines = [output_title_line, border_line, 
             gross_profit_line, number_of_months_line,
             mean_profit_line, worst_loss_line,
             loss_months_line]
output_path = os.path.join('analysis', 'financial_analysis.txt')
with open (output_path, 'w') as output_file:
    for line in all_lines:
        output_file.write(line)
        output_file.write('\n')