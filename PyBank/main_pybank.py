import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#def sum(data):
    #month_total = {"month":data[0], "profit":data[1]}

with open(csvpath, newline='',encoding='UTF-8') as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=',')
    data_header = next(budget_csv)



    date_list = []
    profit_losses = []
    
    for row in budget_csv:
        
        date_list.append(row[0])
        
        profit_losses.append(row[1])

    
    #sum_profit = sum(int(profit_losses))

    print(len(date_list))
    print(profit_losses)
    #print(len(date_list))    
    #sum_month = len(date_list) -1
    #print(sum(int(total_profit)))
   
    #print(sum_month)
    
        
