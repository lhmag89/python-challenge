import os
import csv

csvdata = os.path.join("Resources","budget_data.csv")

with open(csvdata) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    first_row = next(csvreader)
    totmonths = 0
    total = 0
    months = []
    profit = []
    changes = []
    for row in csvreader:
        profit.append(int(row[1]))
        months.append(row[0])
        totmonths = totmonths + 1
        total = total + int(row[1])
    for x in range(1,totmonths):
        monthlyChange = profit[x]- profit[x-1]
        changes.append(int(monthlyChange))
    totalChange = sum(changes)
    aveChange = round(totalChange/len(changes),2)
    maxIncrease = max(changes)
    maxInd = changes.index(maxIncrease) + 1
    maxDecrease = min(changes)
    minInd = changes.index(maxDecrease) + 1

    text = f"""
    Financial Analysis
    _____________________________________________________
    Total Months: {totmonths}
    Total: ${total}
    Average Change: ${aveChange}
    Greatest Increase in Profits: {months[maxInd]} (${changes[maxInd-1]})
    Greatest Decrease in Profits: {months[minInd]} (${changes[minInd-1]})
    """
print(text)
file = open('analysis/financial_analysis.txt', 'w')
file.write(text)
file.close()