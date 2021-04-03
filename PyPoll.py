#Open the data file.
#Write down the names of all the candidates.
#Add a vote count for each candidate.
#Get the total votes for each candidate.
#Get the total votes cast for the election.

#import datetime as dt
#now = dt.datetime.now()
#print("this time:", now)

import csv
import os
#imports csv fule and dir is the directory
#file_variable = open(filename, mode)
# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
#election_data = open(file_to_load, 'r')

# Close the file.
#election_data.close()
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

# Using the open() function with the "w" mode we will write data to the file.
# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
   
    
    #txt_file.write("Arapahoe\n, Denver,\n Jefferson")

