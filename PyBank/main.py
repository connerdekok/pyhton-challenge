#Import os/csv
import os
import csv

# Path to your CSV file
csv_path = (r'F:\bootcamp_work\python-challenge\PyBank\Resources\budget_data.csv')

#Initilize Variables/Also set them to 0 so counts start correctly
Total_Months = 0
Total = 0
Profit_Loss = 0
Profit_Changes = []
Greatest_Increase = ["", 0]   #Add Date with greatest increase and set count to 0
Greatest_Decrease = ["", 0]   #Add Date with greatest decrease and set count to 0
Change = 0


# Open and read the CSV file
with open (csv_path, 'r') as csv_file:

    # Create a CSV reader
    csvreader = csv.reader(csv_file, delimiter=',')

    # Skip the header row
    csv_header = next(csvreader)
    

    # Process each row
    for row in csvreader:
        Total_Months += 1   # Add up Total Months
        Current_profit = int(row[1])  #Find Profit/Loss
        Total += Current_profit  #Calculate Total profits

        
        #Calculate Changes in profit/Loss
        if Total_Months > 1:
            Change = Current_profit - Profit_Loss
            Profit_Changes.append(Change)

        Profit_Loss = Current_profit

        #Calculate Greatest Increase
        if Change > Greatest_Increase[1]:
            Greatest_Increase [0] = row[0]
            Greatest_Increase[1] = Change

        #Calculate Greatest Decrease 
        if Change < Greatest_Decrease[1]:
            Greatest_Decrease [0] = row[0]
            Greatest_Decrease[1] = Change

#Post Average Change
Average_Change = sum(Profit_Changes) / len(Profit_Changes)  #Take sum divided by the count

#Print Statments in order of examples with correct spacing
print("Financial Analysis")

print("-------------------------")

print(f'Total Months: {Total_Months}')
print(f'Net total Profit/Losses: ${Total}')
print(f"Average Change: ${Average_Change:.2f}")
print(f"Greatest Increase In Profits: {Greatest_Increase[0]} ${Greatest_Increase[1]}")
print(f"Greatest Decrease In Profits: {Greatest_Decrease[0]} ${Greatest_Decrease[1]}")
      

#Export Text file 
import os
import csv


# Specify the file to write to
