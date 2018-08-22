# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 22:10:57 2018

@author: kambl
"""

#Dependencies
import os
import csv

#path to the csv file
pyBank_path = os.path.join ('..', 'Resources', 'budget_data.csv')
output_path = os.path.join ('..','Resources', 'pybankresults.csv')

#opening the csv file with built-in open function
#Using with ..as to lock the file resource    

with open (pyBank_path, newline='') as csvfile:
    #Reading from the csv file
    csv_reader = csv.reader(csvfile, delimiter= ',')
    #skipping the header 
    header = next(csv_reader)
    
    total_months = 0
    net_profit_loss = 0
    averages = []
    sumofchanges = 0
    greatest_increase = 0
    greatest_decrease = 0
    
    
    for i,row in enumerate(csv_reader):
        total_months += 1
        net_profit_loss += int(row[1])
        
        
        if i==0:
            current = int(row[1])
        else:
            next_number = int(row[1])
            change = next_number - current
            sumofchanges += change
            averages.append(change)
            current = int(row[1])        
            if change > greatest_increase:
                greatest_increase = change
                increase_date = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                decrease_date = row[0]
 
with open (output_path, 'w') as csvw_file:
    csvw_file.write("Financial Analysis\n")
    csvw_file.write("----------------------------------------------------\n")
    csvw_file.write(f'Total Months: {total_months}\n')
    csvw_file.write(f'Total: ${net_profit_loss}\n')
    csvw_file.write(f'Average Change: ${round(sumofchanges/len(averages),2)}\n') 
    csvw_file.write(f'Greatest Increase in Profits: {increase_date} (${greatest_increase})\n')
    csvw_file.write(f'Greatest Decrease in Losses: {decrease_date} (${greatest_decrease})\n')
     

print("")
print("Financial Analysis")
print("----------------------------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${net_profit_loss}')
print(f'Average Change: ${round(sumofchanges/len(averages),2)}') 
print(f'Greatest Increase in Profits: {increase_date} (${greatest_increase})')
print(f'Greatest Decrease in Losses: {decrease_date} (${greatest_decrease})')

