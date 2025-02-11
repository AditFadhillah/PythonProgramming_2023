import timeit

from handin4 import wordfile_to_list
from handin4 import wordfile_differences_linear_search
from handin4 import wordfile_differences_binary_search
from handin4 import wordfile_to_dict
from handin4 import wordfile_differences_dict_search

# define the file paths
british_filename = 'british-english'
american_filename = 'american-english'

# call wordfile_to_list function
wordlist_british = wordfile_to_list(filename=british_filename)
wordlist_american = wordfile_to_list(filename=american_filename)

# print statements to verify the word lists
print("British English Word List:")
print(wordlist_british)
print("American English Word List:")
print(wordlist_american)

# initialize the timer and call wordfile_differences_linear_search function
start_time = timeit.default_timer()
differences_linear_search = wordfile_differences_linear_search(file1=british_filename, file2=american_filename)
time_spent_linear_search = timeit.default_timer() - start_time

# print the results
print("Differences (Linear Search):")
print(differences_linear_search)
print("Time Spent (Linear Search):", time_spent_linear_search, "seconds")

# initialize the timer and call wordfile_differences_linear_search function
start_time = timeit.default_timer()
differences_binary_search = wordfile_differences_binary_search(file1=british_filename, file2=american_filename)
time_spent_binary_search = timeit.default_timer() - start_time

# print the results
print("Differences (Binary Search):")
print(differences_binary_search)
print("Time Spent (Binary Search):", time_spent_binary_search, "seconds")

# call wordfile_to_dict function
worddict_american = wordfile_to_dict(filename=british_filename)

print("American English Word Dictionary:")
print(worddict_american)

# initialize the timer and call wordfile_differences_linear_search function
start_time = timeit.default_timer()
differences_dict_search = wordfile_differences_dict_search(british_filename, american_filename)
time_spent_dict_search = timeit.default_timer() - start_time

# print the results
print("Differences (Dictionary Search):")
print(differences_dict_search)
print("Time Spent (Dictionary Search):", time_spent_dict_search, "seconds")