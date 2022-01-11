import csv
import os

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

gross_profit = get_total(data)
print(f"The Gross Annual Profit is $" + str(gross_profit))


# Count months
def count_months(data):
    months = 0
    for month in data[1:]:
        months += 1
    return months

number_of_months = count_months(data)
print(f"Gross profit was earned over " + str(number_of_months) + " months")


# Get Average Profit Per Month
def average_profit(gross_profit, number_of_months):
    return round(gross_profit/number_of_months,2)

average_profit = average_profit(gross_profit, number_of_months)
print(f"The Average Price Per Month is $" + str(average_profit))


# Find and count the negative profit months
def count_negative_profit_months(data):
    negative_months = 0
    for amount in data[1:]:
        if int(amount[1]) < 0:
            negative_months += 1
    return negative_months

loss_months = count_negative_profit_months(data)
print(f"There were " + str(loss_months) + " months with negative profit")


# Report Best Month
def best_month(data):
    highest_profit = 0
    best_month = 0
    for amount in data[1:]:
        if int(amount[1]) > int(highest_profit):
            highest_profit = amount[1]
            best_month = amount[0]

    return f"The Best Month on Record is " + str(best_month) + " had a profit of $" + str(highest_profit)

print(best_month(data))


# Report Worst Month
def worst_month(data):
    worst_loss = 0
    worst_month = 0
    for amount in data[1:]:
        if int(amount[1]) < int(worst_loss):
            worst_loss = amount[1]
            worst_month = amount[0]

    return f"The Worst Month on Record is " + str(worst_month) + " had a profit of $" + str(worst_loss)

print(worst_month(data))