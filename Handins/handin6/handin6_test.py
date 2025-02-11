import pandas as pd
from handin6 import find_palindromes

# Part 1.1
print("Part 1.1")
# Read the British English file into a dataframe
df_british = pd.read_csv('british-english', header=None, names=['word'], keep_default_na=False)

# Call the find_palindromes function on the dataframe
palindromes = find_palindromes(df_british)

# Print the resulting dataframe
print(palindromes)

#Part 1.2
print("\nPart 1.2")
from handin6 import find_words_starting_with

# Read the British English file into a dataframe
df_british = pd.read_csv('british-english', header=None, names=['word'], keep_default_na=False)

# Call the find_words_starting_with function with the prefix "congra"
matching_words = find_words_starting_with(df_british, "congra")

# Print the resulting dictionary
print(matching_words)
