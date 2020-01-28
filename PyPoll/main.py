#Import my dependencies
import csv
import os
#Load the files - both input and output
path_to_folder = "Resources"
text_file = "election_results.txt"
csvpath = os.path.join(path_to_folder, "election_data.csv")
output_path= os.path.join(path_to_folder, "election_results.txt")
#Set my variables and lists
votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}
#Read the csv
with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)

#Loop data for list appending
    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]

        if row["Candidate"] not in candidate_options:

            candidate_options.append(row["Candidate"])
            candidate_votes[row["Candidate"]] = 1

        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1
#Pick Winner
    if (votes > winner_votes):
        greatest_votes[1] = candidate_votes
        greatest_votes[0] = row["Candidate"]
#print information
print("Election Results")    
print("-------------------------")    
print("Total Votes " + str(votes))    
print("-------------------------")
#results    
for candidate in candidate_votes:        
    print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
candidate_votes
winner = sorted(candidate_votes.items(),)
#results
print("-------------------------")
print("Winner: " + str(winner[1]))
print("-------------------------")

# # Output Files
with open(output_path, "w") as text_file:
    text_file.write("Election Results")
    text_file.write("\n")
    text_file.write("-------------------------")
    text_file.write("\n")
    text_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    text_file.write(str(winner))
    text_file.write("\n")
    text_file.write("-------------------------")
    text_file.write("\n")
    text_file.write("Winner: " + str(winner[0]))
    text_file.write("\n")
    text_file.write("Total Votes " + str(votes))










