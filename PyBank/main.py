#pybank

#import modules
import os, csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")

#open and read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#skip header
csvheader = next(csvfile)
dates = csvfile[0]
profits = csvfile[1]

total_months = len(dates[0])



# total number of months in the dataset
# net total amount of profit/losses
# net average of profit/losses
# greatest inc in profit for the entire period
# greatest dec in profit for the entire period
#print to terminal
#export text file