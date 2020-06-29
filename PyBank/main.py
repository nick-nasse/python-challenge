#import modules
import csv

#file path
budget_csv = "Resources/budget_data.csv"

#Variables 
total_months = 0

date = []
profit = []

profit_loss = []

last_month = 0

with open(budget_csv, "r+") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    
    for row in csv_reader:
        total_months += 1

        current_month = int(row[1])

        
        change = current_month - last_month
        
        if last_month != 0:
            profit_loss.append(int(change))
        
        date.append(str(row[0]))
        profit.append(int(row[1]))
        last_month = current_month





avg_change = sum(profit_loss) / len(profit_loss)
format_avg_change = "{:.2f}".format(avg_change)

profit_loss.insert(0,0)
zippy = zip(date, profit_loss)

diction = dict(zippy)

overall_profit_loss = sum(profit)


max_key = max(diction, key=diction.get)
min_key = min(diction, key=diction.get)

max_result = diction.get(max_key)
min_result = diction.get(min_key)


print(f"Financial Analysis")
print(f"------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${overall_profit_loss}")
print(f"Average Change: ${format_avg_change}")
print(f"Greatest Increase in Profits: {max_key} at ${max_result}")
print(f"Greatest Decrease in Profits: {min_key} at ${min_result}")

text_path = "Analysis/PyBank_Results.txt"

text_file = open(text_path, "w") 
text_file.write(f"Financial Analysis")
text_file.write("\n")
text_file.write(f"------------------------------------")
text_file.write("\n")
text_file.write(f"Total Months: {total_months}")
text_file.write("\n")
text_file.write(f"Total: ${overall_profit_loss}")
text_file.write("\n")
text_file.write(f"Average Change: ${format_avg_change}")
text_file.write("\n")
text_file.write(f"Greatest Increase in Profits: {max_key} at ${max_result}")
text_file.write("\n")
text_file.write(f"Greatest Decrease in Profits: {min_key} at ${min_result}")
text_file.write("\n")
text_file.close() 