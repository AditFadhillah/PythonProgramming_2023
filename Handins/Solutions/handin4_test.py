import handin4
import timeit

# Hardcoded filenames
filename1 = 'british-english'
filename2 = 'american-english'

# Q1. wordfile_to_list
wordlist_british = handin4.wordfile_to_list(filename1)
wordlist_american = handin4.wordfile_to_list(filename2)

# Q2. Linear search
start_time = timeit.default_timer()
differences_linear_search = handin4.wordfile_differences_linear_search(filename1, filename2)
time_spent_linear_search = timeit.default_timer() - start_time

print(len(differences_linear_search), time_spent_linear_search)


# Q3. Binary search
start_time = timeit.default_timer()
differences_binary_search = handin4.wordfile_differences_binary_search(filename1, filename2)
time_spent_binary_search = timeit.default_timer() - start_time

print(len(differences_binary_search), time_spent_binary_search)


#Q4. wordfile_to_dict
worddict_american = handin4.wordfile_to_list(filename2)


# Q5. Dictionary search
start_time = timeit.default_timer()
differences_dict_search = handin4.wordfile_differences_dict_search(filename1, filename2)
time_spent_dict_search = timeit.default_timer() - start_time

print(len(differences_dict_search), time_spent_dict_search)


