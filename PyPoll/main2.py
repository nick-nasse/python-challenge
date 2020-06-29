#import modules
import csv

#file path
election_path = "Resources/election_data.csv"

#Variables 

total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0 

with open(election_path, "r") as csvfile:
    election_csv = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    
    for row in election_csv:
        total_votes += 1

        if row[2] == "Khan":
            khan_votes += 1
        
        elif row[2] == "Correy":
            correy_votes += 1 
        
        elif row[2] == "Li":
            li_votes += 1
        
        elif row[2] == "O'Tooley":
            otooley_votes += 1
    

khan_percentage = "{:.2f}".format(khan_votes / total_votes * 100)

correy_percentage = "{:.2f}".format(correy_votes / total_votes * 100)

li_percentage = "{:.2f}".format(li_votes / total_votes * 100)

otooley_percentage = "{:.2f}".format(otooley_votes / total_votes * 100)

print(f"Election Results")
print(f"------------------------------------")
print(f"Total Votes: {total_votes}")
print(f"------------------------------------")
print(f"Khan: {khan_percentage}% ({khan_votes})")
print(f"Correy: {correy_percentage}% ({correy_votes})")
print(f"Li: {li_percentage}% ({li_votes})")
print(f"O'Tooley: {otooley_percentage}% ({otooley_votes})")
print(f"------------------------------------")

if khan_votes > correy_votes and khan_votes > li_votes and khan_votes > otooley_votes:
    print("Winner: Khan")
elif correy_votes > khan_votes and correy_votes > li_votes and correy_votes > otooley_votes:
    print("Winner: Correy")
elif li_votes > khan_votes and li_votes > correy_votes and li_votes > otooley_votes:
    print("Winner: Li")
elif otooley_votes > khan_votes and otooley_votes > li_votes and otooley_votes > correy_votes:
    print("Winner: O'Tooley")

print(f"------------------------------------")

winner = "Khan"

text_path = "Analysis/PyPoll_Results.txt"

text_file = open(text_path, "w") 
text_file.write(f"Election Results")
text_file.write("\n")
text_file.write(f"------------------------------------")
text_file.write("\n")
text_file.write(f"Total Votes: {total_votes}")
text_file.write("\n")
text_file.write(f"------------------------------------")
text_file.write("\n")
text_file.write(f"Khan: {khan_percentage}% ({khan_votes})")
text_file.write("\n")
text_file.write(f"Correy: {correy_percentage}% ({correy_votes})")
text_file.write("\n")
text_file.write(f"Li: {li_percentage}% ({li_votes})")
text_file.write("\n")
text_file.write(f"O'Tooley: {otooley_percentage}% ({otooley_votes})")
text_file.write("\n")
text_file.write(f"------------------------------------")
text_file.write("\n")
text_file.write("Winner: " + winner)
text_file.write("\n")
text_file.write(f"------------------------------------")
text_file.close() 