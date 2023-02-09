# add dependenies
import csv
import os

# assign a variable to load and save a file from a path
in_filename = os.path.join('Resources', 'election_results.csv')
out_filename = os.path.join('analysis', 'election_analysis.txt')

# out_file = open(out_filename, 'w')
    # out_file.write("Counties in the Election")
    # out_file.write("\nArapahoe\nDenver\nJefferson")

# initialize a total vote counter
total_votes = 0

# print the candidate name from each row
candidate_options = []

# declare the empty dictionary
candidate_votes = {}

# winning candidate and winning count tracker 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(in_filename) as election_results:
    file_reader = csv.reader(election_results)
 
    # read the header row
    headers = next(file_reader)

    #print each row in the CSV file
    for row in file_reader: 
        # add to the total vote
        total_votes += 1

        # print the candidate name from each row 
        candidate_name = row[2]

        # if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # begin tracking that condidate's vote count
            candidate_votes[candidate_name] = 0

        # add a vote to that candidates count 
        candidate_votes[candidate_name] += 1

# save the results to our text file
with open(out_filename, "w") as txt_file:

    # print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # save the final vote count to the text file 
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        # retrieve vote count of a candidate and percentage
        votes = candidate_votes[candidate_name] 
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        print(candidate_results)
        # save the candidate results to our text file 
        txt_file.write(candidate_results)

        # determine winning vote, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # print the winning candidates' results to the terminal
    winning_candidate_summary = (
        f"-------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------\n")

    print(winning_candidate_summary)

    # save the winning candidates results to the text file 
    txt_file.write(winning_candidate_summary)
