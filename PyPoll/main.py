
# Read CSV file, process data, write to output file and to terminal
import os
import pathlib
import csv

csvpath = pathlib.Path('Resources/election_data.csv')
winner_report = pathlib.Path('Analysis/winner_report.txt')

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


# create dictionary that counts votes for each candidate
# 
VoteDictionary = {}
for Canidate in CandidateName:
    if Canidate in VoteDictionary:
        VoteDictionary[Canidate] +=1
    else:
        VoteDictionary[Canidate] = 1


print("Total number of votes cast: " + str(Total_Votes))

for key in VoteDictionary:
    value = VoteDictionary[key]
    print("Candidate: " + str(key) +" "+ "{:.2f}".format((value/Total_Votes)*100) +"% "+ str(value))

# find the winner
max_vote_count = max(VoteDictionary.values())
# print(max_vote_count)
for key in VoteDictionary:
    value = VoteDictionary[key]
    if value == max_vote_count:
        winner = key
        print("Winner: " + winner)

# for loop to get each candidate and vote_count for output file
c_name = list(VoteDictionary.keys())
c_votes = list(VoteDictionary.values())


# create output report 
output = (
    f"\n\n"
    f"\nElection Results\n"
    f"----------------------------\n"
    f"Total Votes: {Total_Votes}\n"
    f"----------------------------\n"
    f"{c_name[0]}: {(c_votes[0]/Total_Votes)*100 :.2f}% ({c_votes[0]})\n"
    f"{c_name[1]}: {(c_votes[1]/Total_Votes)*100  :.2f}% ({c_votes[1]})\n"
    f"{c_name[2]}: {(c_votes[2]/Total_Votes)*100  :.2f}% ({c_votes[2]})\n"
    f"{c_name[3]}: {(c_votes[3]/Total_Votes)*100  :.2f}% ({c_votes[3]})\n"
    f"----------------------------\n"
    f"Winner: {winner} \n"
    f"----------------------------\n"
    f"\n\n"
    )

# hello 
# Export the results to text file

outfile = open(winner_report, 'w')
outfile.write(output)
outfile.close()

