import os
from pathlib import Path

import csv

# some reason my python environment path will not catch my python-challenge directory correctly
csvpath = Path('/Users/henrywycislo/DataClass/python-challenge/PyBank/Resources/budget_data.csv')

#csvpath = Path('../Resources/budget_data.csv')

# read the file 
with open(csvpath, "r") as csvfile:
    # specify the delimiter and variable to hold data from file 
    csvreader = csv.reader(csvfile, delimiter =',')
    print(csvreader)

    # read the header 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #read each row 
    for row in csvreader:
        print(row)
        thedate = row(0)
        thePL = row(1)
print(thedate)
print(thePL)
