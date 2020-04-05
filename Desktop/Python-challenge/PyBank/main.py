# Credit where credits is deserved. Jon, David and Laura helped me out a lot with this script.
# I also used the following https://github.com/paulXLV/python-challenge/blob/master/PyBank/main.py
# and https://github.com/buitron/python-challenge/blob/master/PyBank/main.py and https://github.com/c-l-nguyen/python-challenge/tree/master/PyBank
# Loading libraries csv and os
import csv
import os
# Defining file paths for the input and output
budget_csv = os.path.join("Resources", "budget_data.csv")
budget_output_txt = os.path.join("Resources", "Budget_output.txt")
# setting initinal variables to zero and string
TotalMonths = 0
GrossProfit = 0
Months = []
NetProfit = []
# open CSV file and iterate thru rows to calculate Financial Analysis
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    # the follwing will count the number of months, sum up the GrossProfit
    # Append will add Profit and month values the the list created above
    for row in csvreader:
        TotalMonths +=1
        GrossProfit += int(row[1])
        NetProfit.append(int(row[1]))
        Months.append(row[0])
# Then calculated values are printed to terminal and a text file
print("\nFinancial Analysis", "\n" + "-" * 60)
print("Total Months", TotalMonths)
print("Total Revenue: $", GrossProfit)
TextFile=open(budget_output_txt,"w")
# The \n in the string tells the text writer to start a new line.
TextFile.write(f"\nFinancial Analysis")
TextFile.write(f"\n" + "-" * 60)
TextFile.write(f"\nTotal Months ")
TextFile.write(f"{TotalMonths}")
TextFile.write(f"\nTotal Revenue: $")
TextFile.write(f"{GrossProfit}")
'''
I want to setup my loop as follow, but the script just wouldn't work
MonthCount = 0
Revenue = 0
InitialValue = 0
TotalRevenue = 0
Months = []
Profit = []
with open(budget_input,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader)
    for row in csvreader:
        MonthCount +=1 
        Revenue += (int(row[1]))
        TotalRevenue += (int(Revenue))-InitialValue
        InitialValue = int(row[1])
        Months.append(str(row[0]))
        Profit.append(str(row[1]))
        '''
# We can't loop thru the csv twice with the same text reader, so i am going to make a list
# and iterate thru that list instead.
# Calculate the difference between months and store in some variable
# Calculate the average change (profit final - profit initial)/ total months
# And prints a formated value to terminal and textfile
IDontKnowWhatToNameThis = []
for i in range(TotalMonths-1):
    IDontKnowWhatToNameThis.append(NetProfit[i+1]-NetProfit[i])
AverageDelta = sum(IDontKnowWhatToNameThis) / (TotalMonths-1)
AverageDelta_formatted = round(AverageDelta,2)
print("Average Change: $", AverageDelta_formatted)
TextFile.write(f"\nAverage Change: $")
TextFile.write(f"{AverageDelta_formatted}")
# Index or find the row with largest and smallest values 
MaxFactor = IDontKnowWhatToNameThis.index(max(IDontKnowWhatToNameThis))
MinFactor = IDontKnowWhatToNameThis.index(min(IDontKnowWhatToNameThis))
# find greatest profit increases or decreases and the months in which they occured
MostProfitableProfits = IDontKnowWhatToNameThis[MaxFactor]
LeastProfitableProfits = IDontKnowWhatToNameThis[MinFactor]
MostProfitableProfitMonths = Months[MaxFactor+1]
LeastProfitableProfitMonths = Months[MinFactor+1]
print(f"Greatest Increase in Profits: {MostProfitableProfitMonths} (${MostProfitableProfits})")
print(f"Greatest Decrease in Profits: {LeastProfitableProfitMonths} (${LeastProfitableProfits})")
TextFile.write(f"\nGreatest Increase in Profits: {MostProfitableProfitMonths} (${MostProfitableProfits})")
TextFile.write(f"\nGreatest Decrease in Profits: {LeastProfitableProfitMonths} (${LeastProfitableProfits})")
