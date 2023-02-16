#pybank

#import modules
import os, csv

csvpath = os.path.join("..","python-challenge","budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)

# total number of months in the dataset
# net total amount of profit/losses
# net average of profit/losses
# greatest inc in profit for the entire period
# greatest dec in profit for the entire period
#print to terminal
#export text file