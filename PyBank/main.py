#pybank

#import modules
import os, csv
csvpath = os.path.join("C:\\Users\\itsy7\\OneDrive\\Documents\\GitHub\\python-challenge\\PyBank\\Resources\\budget_data.csv")

#Create variables for things we need
dates = 0
totalprofits = 0
net_change_list = []
greatest_inc_list =["", -100000000000]
greatest_dec_list =["", 1000000000000]

#open and read csv file and skip header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader) 
    budgetdata = list(csvreader)
    previous_net = int(budgetdata[0][1])
    
# net total amount of profit/losses
    for i in budgetdata:
        dates += 1
        totalprofits += int(i[1])

# rolling change of profit/losses 
        change = int(i[1]) - previous_net
        previous_net = int(i[1])
        net_change_list += [change]

      
# greatest inc/dec in profit for the entire period
        greatest_inc = max(net_change_list)
        greatest_dec = min(net_change_list)

        if change == greatest_inc:
            greatest_inc_list = [i[0],greatest_inc]
        if change == greatest_dec:
            greatest_dec_list = [i[0],greatest_dec]


#Calculations:
    average = sum(net_change_list)/(dates - 1)
    average = round(average,2)                

#print to terminal
print(f"""
Financial Analysis
----------------------------
Total Months: {dates}
Total: ${totalprofits}
Average Change: ${average}
Greatest Increase in Profits: {greatest_inc_list[0]}  (${greatest_inc_list[1]})
Greatest Increase in Profits: {greatest_dec_list[0]}  (${greatest_dec_list[1]})""")

#export text file
with open("C:\\Users\\itsy7\\OneDrive\\Documents\\GitHub\\python-challenge\\PyBank\\Analysis\\Analysis.csv","w", newline="") as csvfile:
    csvfile.write(f"""
Financial Analysis
----------------------------
Total Months: {dates}
Total: ${totalprofits}
Average Change: ${average}
Greatest Increase in Profits: {greatest_inc_list[0]}  (${greatest_inc_list[1]})
Greatest Increase in Profits: {greatest_dec_list[0]}  (${greatest_dec_list[1]})""")
