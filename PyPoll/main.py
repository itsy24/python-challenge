#pypoll

#import modules
import os, csv

csvpath = os.path.join("C:\\Users\\itsy7\\OneDrive\\Documents\\GitHub\\python-challenge\\PyPoll\\Resources\\election_data.csv")

#Create Variables
total_votes = 0
candidate_list = []
votercount1= 0
votercount2 = 0
votercount3 = 0
winner = 0


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
        if i[2] == voter3:
            votercount3 += 1       

# % votes/candidate
    percent1 = (votercount1/total_votes) * 100
    percent1 = round(percent1,3)

    percent2 = (votercount2/total_votes) * 100
    percent2 = round(percent2,3)

    percent3 = (votercount3/total_votes) * 100
    percent3 = round(percent3,3)
    

# Winner based on popular vote
    if votercount1 > votercount2 and votercount1 > votercount3:
        winner = voter1 
    elif votercount2 > votercount1 and votercount2 > votercount3:
        winner = voter2
    elif votercount3 > votercount1 and votercount3 > votercount2:
        winner = voter3

#print to terminal
print(f""" 
Election Results
-----------------------
Total Votes: {total_votes}   
-----------------------
{candidate_list[0]}: {percent1}% ({votercount1})
{candidate_list[1]}: {percent2}% ({votercount2})
{candidate_list[2]}: {percent3}% ({votercount3})
-----------------------
Winner: {winner}
-----------------------""")
#export text file
with open("C:\\Users\\itsy7\\OneDrive\\Documents\\GitHub\\python-challenge\\PyPoll\\Analysis\\Analysis.csv","w", newline="") as csvfile:
    csvfile.write(f""" 
Election Results
-----------------------
Total Votes: {total_votes}   
-----------------------
{candidate_list[0]}: {percent1}% ({votercount1})
{candidate_list[1]}: {percent2}% ({votercount2})
{candidate_list[2]}: {percent3}% ({votercount3})
-----------------------
Winner: {winner}
-----------------------""")