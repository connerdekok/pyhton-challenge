#Import os/csv
import os
import csv

# Path to your CSV file
#This path is to an extrenal drive I have my class documents stored 
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#Initilize Variables/Also set them to 0 so counts start correctly
Total_Months = 0 
Total = 0
Profit_Loss = 0  #profits or losses
Profit_Changes = []  #classifies values as a list
Greatest_Increase = ["", 0]   #Add Date with greatest increase and set count to 0
Greatest_Decrease = ["", 0]   #Add Date with greatest decrease and set count to 0
Change = 0  #Sets value placeholder


# Open and read the CSV file
with open(budget_data_csv) as csv_file:

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

 
#Gives file path to create text file/ And print results in the terminal
    #State text file/folder path to store text document
output_file_path = os.path.join("analysis", "PyBank_Analysis")  
with open(output_file_path, 'w') as f:

#Print Statments in order of examples 
    print("Financial Analysis", file=f)  # For f lines to print to text file
    print("Financial Analysis") #to print results to terminal
    print("-------------------------", file =f) # For f lines to print to text file
    print("-------------------------") #to print results to terminal
    
    print(f"Total Months: {Total_Months}", file=f) # For f lines to print to text file
    print(f"Total Months: {Total_Months}") #to print results to terminal
    print(f"Total: ${Total}", file=f) # For f lines to print to text file
    print(f"Total: ${Total}") #to print results to terminal
    print(f"Average Change: ${Average_Change:.2f}", file=f) # For f lines to print to text file
    print(f"Average Change: ${Average_Change:.2f}") #to print results to terminal
    print(f"Greatest Increase In Profits: {Greatest_Increase[0]} (${Greatest_Increase[1]})", file=f) # For f lines to print to text file
    print(f"Greatest Increase In Profits: {Greatest_Increase[0]} (${Greatest_Increase[1]})") #to print results to terminal
    print(f"Greatest Decrease In Profits: {Greatest_Decrease[0]} (${Greatest_Decrease[1]})", file=f) # For f lines to print to text file
    print(f"Greatest Decrease In Profits: {Greatest_Decrease[0]} (${Greatest_Decrease[1]})") #to print results to terminal
      