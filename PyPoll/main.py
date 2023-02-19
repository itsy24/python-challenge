#pypoll

#import modules
import os, csv
from itertools import cycle

csvpath = os.path.join("C:\\Users\\itsy7\\OneDrive\\Documents\\GitHub\\python-challenge\\PyPoll\\Resources\\election_data.csv")

#Create Variables
total_votes = 0
candidate_list = []
votercount1= 0
votercount2 = 0
votercount3 = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader) 
    election_data = list(csvreader)

#total votes casted / candidate names
    for i in election_data:
        total_votes += 1
        candidate_name = i[2]
        if i[2] not in candidate_list:
            candidate_list += [i[2]]

# total votes/candidate
    for i in election_data:
        voter1 = candidate_list[0]
        voter2 = candidate_list[1]
        voter3 = candidate_list[2]
        if i[2] == voter1:
            votercount1 += 1
        if i[2] == voter2:
            votercount2 += 1
        if i[2] == voter2:
            votercount3 += 1           

# % votes/candidate
    percent1 = (votercount1/total_votes) * 100
    percent1 = round(percent1,3)

    percent2 = (votercount2/total_votes) * 100
    percent2 = round(percent2,3)

    percent3 = (votercount3/total_votes) * 100
    percent3 = round(percent2,3)
    


    



# Winner based on popular vote

#print to terminal
print(f""" 
Election Results
-----------------------
Total Votes: {total_votes}   
-----------------------

                               """)
#export text file