import os
from pathlib import Path
import datetime
import csv

# some reason my python environment path will not catch my python-challenge directory correctly
csvpath = Path('/Users/henrywycislo/DataClass/python-challenge/PyBank/Resources/budget_data.csv')

#csvpath = os.path.join('..','Resources','budget_data.csv')

# read the file 
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header:  {csv_header}")

    for row in csvreader:
        PLDate = row(0)
        PLAmount = float(row(1))
        print(PLDate)
        print(PLAmount)
        