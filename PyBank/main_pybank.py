import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')


#def data_stat(budget_data):

    
    
   # profit_loss_total = profit_loss.sum()

with open(csvpath, newline='',encoding='UTF-8') as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=',')
    data_header = next(budget_csv)
    
    for row in budget_csv:
        print(row)
        print(data_header)
        #month_count = len(month)
    #profit_total = sum(profit)

        #print(f"Total Month: {month_count}")
    #print(f"Total Profit: {profit_total} ")
        