import os
from pathlib import Path
import datetime
import csv

csvpath = Path('Resources/budget_data.csv')

# lists to store data

PLDate = []
PLAmount = []
total_PL = 0 


# read the file 
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header:  {csv_header}")

    for row in csvreader:
        PLDate.append(row[0])
        total_PL += (int(row[1]))
        PLAmount.append (int(row[1]))

max_amount = max(PLAmount)

# create dictionay from two lists using zip 
PLDictionary = dict(zip(PLAmount,PLDate))
#print(PLDictionary)

# find date for max amount 
# max_date = PLDictionary.get(max_amount)
max_date = PLDictionary.get(max(PLAmount))
print(max_date +"," +str(max_amount))


total_months = len(PLDate)
#test_profit_month = PLDictionary(str(max(PLAmount)))
#print(test_profit_month)
#total_PL = sum(float(PLAmount))
print("Total Months: " + str(total_months))
print("Total: $" + str(total_PL))
print("Average Change: " + str(total_PL/total_months))
print("Greatest Increase in Profits: " + max_date +" ("+str(max_amount) +")")
print("min :" + str(min(PLAmount)))
#print(PLDate,PLAmount)   
# hi
