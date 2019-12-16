import os
import csv

csv_path = os.path.join("Resources", "election_data.csv")

with open(csv_path, newline='',encoding='UTF-8') as csvfile:
    poll_csv = csv.reader(csvfile, delimiter=',')
    data_header = next(poll_csv)

    vote_casted = []
    candiate = []

    for row in poll_csv:
        vote_casted.append(row[0])
        
        candidate.append(row[2]) for row[2] in candidate if row[2] != candidate
              
    print(len(candidate))
    print(data_header)
    print(f"Total Number of Votes Cast: {len(vote_casted)}")

