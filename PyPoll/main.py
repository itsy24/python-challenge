#pypoll

#import modules
import os, csv

csvpath = os.path.join("C:\\Users\\itsy7\\OneDrive\\Documents\\GitHub\\python-challenge\\PyPoll\\Resources\\election_data.csv")

#Create Variables
total_votes = 0
candidate_list = []
votes= 0
votes2 = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader) 
    election_data = list(csvreader)

    for i in election_data:
        total_votes += 1
        if i[2] not in candidate_list:
            candidate_list += [i[2]]
        if i[2] == candidate_list[0]:
            votes += 1
        if i[2] == candidate_list[0]:
            votes += 1
      
print(candidate_list)
print(votes)
    

# total number of months in the dataset
# net total amount of profit/losses
# net average of profit/losses
# greatest inc in profit for the entire period
# greatest dec in profit for the entire period
#print to terminal
#export text file