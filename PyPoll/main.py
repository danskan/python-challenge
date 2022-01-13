import os
import csv

# Read the file and store to variable
csvpath = os.path.join('Resources', 'election_data.csv')
with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    data = list(csvreader)

# Calculate the total number of votes cast
def get_total_votes(data):
    total_votes = 0
    for line in data[1:]:
        total_votes += 1
    return total_votes

# Product a list of candidates who received votes
def get_list_of_candidates(data):
    candidates_list = []
    vote_list = []
    for line in data[1:]:
        if line[2] not in candidates_list:
            candidates_list.append(line[2])
    return candidates_list

# Total Votes Per Candidate
def get_votes_by_candidate(candidates_list, data):
    vote_count = 0
    candidate_votes_list = []
    for candidate in candidates_list:
        for line in data[1:]:
            if candidate == line[2]:
                vote_count += 1
        candidate_votes_list.append(vote_count)
        vote_count = 0
    return candidate_votes_list

# Calculate the percentage of votes each candidate received
def get_candidate_vote_percentage(candidate_vote_list, total_votes):
    percentage_list = []
    for item in candidates_vote_list:
        percentage_list.append(str(round(((item/total_votes)*100),2))+"%")
    return percentage_list

# Find the winning Candidate
def get_winner(candidates_vote_list):
    return candidates_vote_list.index(max(candidates_vote_list))
    

# Call the functions and store the variables
total_votes = get_total_votes(data)
total_votes_line = f'Total Votes: ' + str(total_votes)

candidates_list = get_list_of_candidates(data)
candidates_vote_list = get_votes_by_candidate(candidates_list, data)
percentage_list =get_candidate_vote_percentage(candidates_vote_list, total_votes)
winner_index = get_winner(candidates_vote_list)
winner = candidates_list[winner_index]
winner_line = f'Winner: ' + winner
final_list = list(zip(candidates_list, candidates_vote_list, percentage_list))
title = f'Election Results'
border = f'-----------------'

def all_candidates_output():
    main_body_lines = []
    for candidate in final_list:
        main_body_lines.append(candidate[0] + ": " + candidate[2] + " (" + str(candidate[1]) + " total votes)")
    return main_body_lines

main_body = all_candidates_output()

# Print results to terminal
print(title)
print(border)
print(total_votes_line)
print(border)
for line in main_body:
    print(line)
print(border)
print(winner_line)
print(border)

# Output the results to a text file
output_path = os.path.join('analysis', 'poll_results.txt')
with open (output_path, 'w') as output_file:
        output_file.write(title)
        output_file.write('\n')
        output_file.write(border)
        output_file.write('\n')
        output_file.write(total_votes_line)
        output_file.write('\n')
        output_file.write(border)
        output_file.write('\n')
        for line in main_body:
            output_file.write(line)
            output_file.write('\n')
        output_file.write(border)
        output_file.write('\n')
        output_file.write(winner_line)
        output_file.write('\n')
        output_file.write(border)

