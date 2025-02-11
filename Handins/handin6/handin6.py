import pandas as pd

def find_palindromes(word_dataframe, minimum_length=4):
    # Convert all words to lowercase and remove words with apostrophes
    word_dataframe['word'] = word_dataframe['word'].str.lower()
    word_dataframe = word_dataframe[~word_dataframe['word'].str.contains("'")]

    # Create a boolean mask for palindromes with at least minimum_length characters
    mask = (word_dataframe['word'].str.len() >= minimum_length) & (word_dataframe['word'] == word_dataframe['word'].str[::-1])

    # Filter the dataframe based on the mask
    result_dataframe = word_dataframe[mask]

    return result_dataframe

def find_words_starting_with(word_dataframe, prefix):
    # Convert all words to lowercase and remove words with apostrophes
    word_dataframe['word'] = word_dataframe['word'].str.lower()
    word_dataframe = word_dataframe[~word_dataframe['word'].str.contains("'")]

    # Create an empty dictionary to store the results
    matching_words_dict = {}

    # Iterate through the dataframe to find matching words
    for word in word_dataframe['word']:
        if word.startswith(prefix.lower()):
            length = len(word)
            if length not in matching_words_dict:
                matching_words_dict[length] = []
            matching_words_dict[length].append(word)

    return matching_words_dict
