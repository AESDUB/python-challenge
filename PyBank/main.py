#Import dependencies
import os
import csv
#Load the dataset
path_to_folder = 'Resources'
data_file = 'budget_data.csv'
text_file = 'Financial_Statistics.txt'
input_file = os.path.join(path_to_folder, data_file)
#Set Variables and lists for columns
total_months = []
total_profit = []
monthly_profit_change = []
#Open the csv in read mode
with open(input_file,newline="", encoding="utf-8",) as budget:
    #Store budget data in V csvreader
    csvreader = csv.reader(budget,delimiter=",")
    #Start on second row
    header = next(csvreader)
    
    #Iterate rows in stored data
    for row in csvreader:
    #For the total number of months included, append to total_months list
        total_months.append(row[0])
    #For the net total P/L, sum the second column
        total_profit.append(int(row[1]))
    #Check it worked
    # print(total_months)
    # print(total_profit)
#For the average of changes, iterate through profits of each row 
    for i in range(len(total_profit)-1):
        #append the difference into list monthly_profit_change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
#For greatest increase in profits, find max from monthly_profit_change list
max_increase_month = monthly_profit_change.index(max(monthly_profit_change))+1
#For greatest decrease in profits, find min from monthly_profit_change list
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change))+1
#print results
results = f"""
Financial Analysis
----------------------------
Total Months: {len(total_months)}
Total: ${sum(total_profit)}
Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}
Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max(monthly_profit_change)))})
Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(min(monthly_profit_change)))})
"""
print(results)
#Output files
output_file = os.path.join(path_to_folder, text_file)
with open(output_file,"w") as text_file:
    text_file.write(results)






