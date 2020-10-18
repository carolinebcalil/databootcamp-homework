import os
import csv
import collections
from collections import Counter

voters_candidates = []
votes_per_candidate = []

os.chdir(os.path.dirname(__file__))

filepath = os.path.join("Resources", "election_data.csv")


with open(filepath, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    for row in csv_reader:

        voters_candidates.append(row[2])

    sorted_list = sorted(voters_candidates)
    
    
    arrange_list = sorted_list

    count_candidate = Counter (arrange_list) 
    votes_per_candidate.append(count_candidate.most_common())

    for item in votes_per_candidate:
       
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourth = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')


print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("-------------------------")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})")
print("-------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print("-------------------------")


election_file = os.path.join("Output", "election_data.txt")
with open(election_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
    outfile.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
    outfile.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
    outfile.write(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
    outfile.write("-------------------------\n")   