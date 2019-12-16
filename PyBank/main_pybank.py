import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#def sum(data):
    #month_total = {"month":data[0], "profit":data[1]}

with open(csvpath, newline='',encoding='UTF-8') as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=',')
    #data_header = next(budget_csv)

    date_list = []
    for row in budget_csv:
        
        date_list.append(row[0])

    #print(len(date_list))    
    sum_month = len(date_list) -1
    print(sum_month)
    
        
        #print(date_list) - showed list of date_list
    
    #print(f"Total number of month: {number_of_month}")



#for row in budget_csv:
        
    #print(row[1]) -- tested to see all rows at index 1
    #print(row[0]) -- tested to see all rows at index 0
