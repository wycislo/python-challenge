import os
from pathlib import Path

import csv

curr_path = Path.cwd()
print (curr_path)
#csvpath = Path('/Users/henrywycislo/DataClass/python-challenge/PyBank/Resources/budget_data.csv')

csvpath = Path('../Resources/budget_data.csv')

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
