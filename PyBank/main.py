import os
#from pathlib import Path
import pathlib
import datetime
import csv

csvpath = pathlib.Path('Resources/budget_data.csv')
Analysis_Report = pathlib.Path('Analysis/Profit_Report.txt')

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
min_amount = min(PLAmount)

# create dictionay from two lists using zip 
PLDictionary = dict(zip(PLAmount,PLDate))
#print(PLDictionary)

# find date for max amount 
# max_date = PLDictionary.get(max_amount)
max_date = PLDictionary.get(max(PLAmount))
print(max_date +"," +str(max_amount))
min_date = PLDictionary.get(min(PLAmount))
print(min_date +"," +str(min_amount))

total_months = len(PLDate)
average_change = total_PL/total_months
#test_profit_month = PLDictionary(str(max(PLAmount)))
#print(test_profit_month)
#total_PL = sum(float(PLAmount))
print("Total Months: " + str(total_months))
print("Total: $" + str(total_PL))
print("Average Change: " + str(total_PL/total_months))
print("Greatest Increase in Profits: " + max_date +" ("+str(max_amount) +")")
print("Greatest Increase in Profits: " + min_date +" ("+str(min_amount) +")")



#Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total Amount of Profit / Loss: ${total_PL}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {max_date} (${max_amount})\n"
    f"Greatest Decrease in Profits: {min_date} (${min_amount})\n"
    f"\n\n"
    )

# Print the output (to terminal)
print(output)

# Export the results to text file

outfile = open(Analysis_Report, 'w')
outfile.write(output)
outfile.close()

