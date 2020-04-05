#I felt totaly lost on the Python challenge, so I got a lot of help from Jon, David, Laura and scott, as well as from below
# https://github.com/paulXLV/python-challenge/tree/master/PyPolls, https://github.com/racquesta/python-challenge/tree/master/PyPoll,
# https://github.com/buitron/python-challenge/tree/master/PyPoll and https://github.com/c-l-nguyen/python-challenge/tree/master/PyPoll  
import csv
import os

election_csv = os.path.join("Resources", "election_data.csv")
ElectionResults_txt = os.path.join("Resources", "ElectonResults.txt")

headers = "Voter ID,County,Candidate"
headers = headers.split(",")

TotalVotes = 0
CandidateVotes = {}
# Because I can only read the csv once per reader I used a dictonary reader the first iteration thru.
# I used a dictonary reader, i had to define column headers, and header delimiter
with open(election_csv, 'r', newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",", fieldnames = headers)
    next(csvreader)
    # tally up the total votes and votes per candidate
    for row in csvreader:
        TotalVotes +=1
        # if the candidate is in the dictonary, then add 1. otherwise, create initial entry for candidate
        if CandidateVotes.get(row["Candidate"]) != None:
            CandidateVotes[row["Candidate"]] += 1
        else:
            CandidateVotes[row["Candidate"]] = 1
print("Electon Results", "\n" + "-" * 30)
print("\n TotalVotes:", TotalVotes)
print("\n" + "-" * 30)
TextFile=open(ElectionResults_txt,"w")
TextFile.write(f"\nElection Results")
TextFile.write(f"\n" + "-" * 30)
TextFile.write(f"\nTotalVotes:")
TextFile.write(f"{TotalVotes}")
TextFile.write(f"\n" + "-" * 30) 
# calculate percentage of vote for each candidate and then find the winner
PercentVote = {}
for key, value in CandidateVotes.items():
    PercentVote[key] = round(CandidateVotes[key]/TotalVotes * 100)
Winner = max(PercentVote, key=PercentVote.get)
for Candidate in CandidateVotes.keys():
    print(f"\n{Candidate}: {PercentVote[Candidate]:.3f}% ({CandidateVotes[Candidate]})")
print("\n" + "-" * 30)
print("\nWinner:", Winner)
# OMG! Why is write a dicronary to a text file so hard!!!! I have to iterate thru my studip dictonary!
for Candidate in CandidateVotes.keys():
    TextFile.write(f"\n{Candidate}: {PercentVote[Candidate]:.3f}% ({CandidateVotes[Candidate]})")
TextFile.write(f"\n" + "-" * 30)
TextFile.write(f"\nWinner: ")
TextFile.write(f"{Winner}")
# I added this bit to run if there was a tie, but there wasn't a tie and it made printing/writing the Winner insane.
# So now it sits here sad and unused.
if len(Winner) > 1:
    for w in range(1, len(Winner)):
        Winner = Winner + ", " + Winner[w]

     
