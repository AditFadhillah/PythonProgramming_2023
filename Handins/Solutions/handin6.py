
def find_palindromes(word_dataframe, minimum_length=4):
    """
    Find palindromes in a Dataframe containing a single column of words.
    We assume the column name to be 'words'
    The function is case-insensitive
    """

    mask1 = word_dataframe['word'].str.lower() == word_dataframe['word'].str.lower().str[::-1]
    mask2 = word_dataframe['word'].str.len() > minimum_length
    mask3 = (~word_dataframe['word'].str.contains("'"))

    return word_dataframe[mask1 & mask2 & mask3]

def find_words_starting_with(word_dataframe, prefix):
    """
    Find words in wordlist starting with specified prefix, ignoring apostrophes
    The function is case-insensitive
    """

    mask1 = word_dataframe['word'].str.lower().str.startswith(prefix.lower())
    mask2 = (~word_dataframe['word'].str.contains("'"))
    df_match = word_dataframe[mask1 & mask2]

    rvalue = {}
    for name, grp in df_match.groupby(df_match['word'].str.len()):
        rvalue[name] = grp['word'].values.tolist()
    return rvalue
