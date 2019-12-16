import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')


def data_stat(budget_data):
    
    date = budget_data[0]
    #profit = int(budget_data[1])

    number_of_month = len(date)
    
    #profit_loss_total

    print(f"Total number of month: {number_of_month}")

    
   # profit_loss_total = profit_loss.sum()

with open(csvpath, newline='',encoding='UTF-8') as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=',')
    data_header = next(budget_csv)

    for row in budget_csv:
        data_stat(row)



        
        
#for row in budget_csv:
        
    #print(row[1]) -- tested to see all rows at index 1
    #print(row[0]) -- tested to see all rows at index 0
