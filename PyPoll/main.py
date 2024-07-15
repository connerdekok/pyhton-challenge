#Import os/csv
import os
import csv

# Path to your CSV file
csv_path =  (r'F:\bootcamp_work\python-challenge\PyPoll\Resources\election_data.csv')

# Initialize Variables
Total_Votes = 0
candidates = {}
Winner = ""
Max_Votes = 0   #sets max votes to 0 


# Open and read the CSV file
with open (csv_path, 'r') as csv_file:

    # Create a CSV reader
    csvreader = csv.reader(csv_file, delimiter=',')

    # Skip the header row
    csv_header = next(csvreader)
    
    # Process each row
    for row in csvreader:
        Total_Votes += 1   # Add up Total Votes
        Candidate_name = row[2] #Find candidate names in csv
        
        #Add up votes for each candidate
        if Candidate_name not in candidates: 
            candidates[Candidate_name] = 1
        else:
            candidates[Candidate_name] += 1

    #Calculate Winner (used microsoft copilot to help find this code with the items tag)
    for Canidate, Votes in candidates.items():
        if Votes > Max_Votes:
            Winner = Canidate
            Max_Votes = Votes

#Print results of total votes and puts election results header
print("Election Results")
print("-------------------------")
print(f'Total Votes: {Total_Votes}')
print("-------------------------")

# Calculate the percentage of votes each candidate won/ This also positions this data in the correct spot like the example
for Candidate, Votes in candidates.items():
    percent = (Votes / Total_Votes) * 100
    print(f'{Candidate}: {percent:.3f}% ({Votes})')
#print spaces and print out the winner of the election
print("-------------------------")
print("Winner: " + Winner)
print("-------------------------")






