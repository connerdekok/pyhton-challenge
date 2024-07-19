#Import os/csv
import os
import csv

# Path to your CSV file
 #This path is to an extrenal drive I have my class documents stored 
election_data_csv = os.path.join("Resources", "election_data.csv")

# Initialize Variables
Total_Votes = 0 
candidates = {} #creates a dictionary that will help keep values together
Winner = ""  #Declare the winner as a string
Max_Votes = 0   #sets max votes to 0 


# Open and read the CSV file
with open(election_data_csv) as csv_file:

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

    #Calculate Winner/ access dictionary
    for Canidate, Votes in candidates.items():   
        if Votes > Max_Votes:
            Winner = Canidate
            Max_Votes = Votes


#Print results of total votes/Text file/Puts election results header
    output_file_path = os.path.join("analysis", "PyPoll_Analysis")  
    with open(output_file_path, 'w') as f:

        print("Election Results", file=f) # For f lines to print to text file
        print("Election Results") #to print results to terminal
        print("-------------------------", file=f) # For f lines to print to text file
        print("-------------------------") #to print results to terminal
        print(f'Total Votes: {Total_Votes}', file=f) # For f lines to print to text file
        print(f'Total Votes: {Total_Votes}') #to print results to terminal
        print("-------------------------", file=f) # For f lines to print to text file
        print("-------------------------") #to print results to terminal

        # Calculate the percentage of votes each candidate won/ Keep these print statements in for loop: to get all 3 candidates listed with the correct information.
        for Candidate, Votes in candidates.items():
            percent = (Votes / Total_Votes) * 100

            print(f'{Candidate}: {percent:.3f}% ({Votes})', file=f) # For f lines to print to text file
            print(f'{Candidate}: {percent:.3f}% ({Votes})') #to print results to termina

        #print spaces and print out the winner of the election
        print("-------------------------", file=f) # For f lines to print to text file
        print("-------------------------") #to print results to terminal
        print("Winner: " + Winner, file=f) # For f lines to print to text file
        print("Winner: " + Winner) #to print results to terminal
        print("-------------------------", file=f) # For f lines to print to text file 
        print("-------------------------")  #to print results to terminal
 





