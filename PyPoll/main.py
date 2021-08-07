# PyBank
# Read CSV file, process data, write to output file and to terminal
import os
from pathlib import Path
import csv


csvpath = Path('Resources\election_data.csv')

# lists to store data

voter_id = []
County = []
CandidateName = []
Total_Votes = 0

with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #skip the header
    next(csvreader)

    for row in csvreader:
        voter_id.append(row[0])
        County.append (row[1])
        CandidateName.append (row[2])
        Total_Votes = Total_Votes +1


# create dictionay that counts votes for each candidate
# PLDictionary = dict(zip(CandidateName,voter_id))
VoteDictionary = {}
for Canidate in CandidateName:
    if Canidate in VoteDictionary:
        VoteDictionary[Canidate] +=1
    else:
        VoteDictionary[Canidate] = 1


print(Total_Votes)

for key in VoteDictionary:
    value = VoteDictionary[key]
    print("Candidate: " + key, value)

# hello 

