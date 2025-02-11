def wordfile_to_list(filename): 
    '''Read a one-word-per-line file into a list'''
    
    # Open file
    word_file = open(filename)
    
    words = []
    for line in word_file:

        # Remove white space at end
        line = line.rstrip()

        # Skip empty lines
        if len(line) == 0:
            continue

        # Append to list
        words.append(line)

    return words


def wordfile_differences_linear_search(filename1, filename2):
    '''Find differences between two one-word-per-line files using linear search'''

    # Call wordfile_to_list on both files
    word_list1 = wordfile_to_list(filename1)
    word_list2 = wordfile_to_list(filename2)

    ids = []
    # Iterate over all words in list1
    for word in word_list1:
        # Iterate over words in  (linear search using in operator)
        if word not in word_list2:
            ids.append(word)

    return ids


def binary_search(sorted_list, element):
    """Search for element in list using binary search.
       Assumes sorted list"""
    # Current active list runs from index_start up to
    # but not including index_end
    index_start = 0
    index_end = len(sorted_list)
    while (index_end - index_start) > 0:
        index_current = (index_end-index_start)//2 + index_start
        if element == sorted_list[index_current]:
            return True
        elif element < sorted_list[index_current]:
            index_end = index_current
        elif element > sorted_list[index_current]:
            index_start = index_current+1
    return False


def wordfile_differences_binary_search(filename1, filename2):
    '''Find overlap between two one-word-per-line files using binary search'''

    # Call wordfile_to_list on both files
    word_list1 = wordfile_to_list(filename1)
    word_list2 = wordfile_to_list(filename2)

    # word_list2 must be sorted for binary search to work
    word_list2.sort()
    
    ids = []
    # Iterate over all words in list1
    for word in word_list1:
        # Iterate over words in  (linear search using in operator)
        if not binary_search(word_list2, word):
            ids.append(word)

    return ids
    

def wordfile_to_dict(filename):
    '''Read a one-word-per-line file into a dictionary (as keys)'''

    # Open file
    word_file = open(filename)
    
    words = {}
    for line in word_file:

        # Remove white space at end
        line = line.strip()

        # Skip empty lines
        if len(line) == 0:
            continue
        
        # Add as key to dictionary
        words[line] = None

    return words


def wordfile_differences_dict_search(filename1, filename2):
    '''Find overlap between two one-word-per-line files using binary search'''

    word_list = wordfile_to_list(filename1)
    word_dict = wordfile_to_dict(filename2)

    ids = []
    # Iterate over all words in list1
    for word in word_list:
        if word not in word_dict:
            ids.append(word)

    return ids
