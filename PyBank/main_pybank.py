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

    

    #print(len(date_list))
    #print(profit_losses)
    
    
    print("Financial Analysis-------------")
    print(f"Total Months: {len(date_list)}")

    #print(f"Total: ${total_profit}")
    #print(f"Average  Change: {average_change}")
    #print(f"Greatest Increase in Profits: {max_increase}")
    #print(f"Greatest Decrease in Profits: {max_decrease}")
    #print(f"Total profit/losses:{total}")
   
   
    
        
