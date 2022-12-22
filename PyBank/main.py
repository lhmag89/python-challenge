#import dependencies
import os
import csv
#create relative filepath
csvdata = os.path.join("Resources","budget_data.csv")
#read csv file
with open(csvdata) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #store header row
    header = next(csvreader)
    
    #convert columns of months and profit/loss to list and make a list for monthly changes
    months = []
    profit = []
    changes = []
    
    #use for loop to append values to lists
    for row in csvreader:
        profit.append(int(row[1]))
        months.append(row[0])
    
    #calculate number of months and total of profit/loss
    totmonths = len(months)
    total = sum(profit)
    
    #loop through profit to find changes per month and append results to a new list of monthly changes
    for x in range(1,totmonths):
        monthlyChange = profit[x]- profit[x-1]
        changes.append(int(monthlyChange))
    
    #run financial analysis calculations
    totalChange = sum(changes)
    aveChange = round(totalChange/len(changes),2)
    maxIncrease = max(changes)
    maxInd = changes.index(maxIncrease) + 1
    maxDecrease = min(changes)
    minInd = changes.index(maxDecrease) + 1

    #format multiline export
    text = f"""
    Financial Analysis
    _____________________________________________________

    Total Months: {totmonths}
    Total: ${total}
    Average Change: ${aveChange}
    Greatest Increase in Profits: {months[maxInd]} (${changes[maxInd-1]})
    Greatest Decrease in Profits: {months[minInd]} (${changes[minInd-1]})
    _____________________________________________________
    """
#export results
print(text)
file = open('analysis/financial_analysis.txt', 'w')
file.write(text)
file.close()