#import modules
import csv

#file path
election_path = "Resources/election_data.csv"

#variables
d = {}
total_votes = 0 

with open(election_path, "r") as csvfile:
    election_csv = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    for row in election_csv:
        total_votes += 1

        if row[2] in d:
            d["%s" % row[2]] += 1

        else: 
            d["%s" % row[2]] = 1


print(f"Election Results")
print(f"------------------------------------")
print(f"Total Votes: {total_votes}")
print(f"------------------------------------")
for key in d:
    print(key,":", "{:.2f}".format(d[key]/total_votes*100), "%", "(", d[key], ")")
print(f"------------------------------------")
print("Winner:", max(d, key=d.get))
print(f"------------------------------------")



text_iteration = []

for key in d: 
    text_iteration.append(f"{key} : {round(d[key]/total_votes*100, 2)}% ({d[key]})")

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
for texty in text_iteration:
    text_file.write(texty)
    text_file.write("\n")
text_file.write(f"------------------------------------")
text_file.write("\n")
text_file.write(f"Winner: {max(d, key=d.get)}")
text_file.write("\n")
text_file.write(f"------------------------------------")