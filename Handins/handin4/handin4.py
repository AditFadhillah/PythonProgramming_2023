"""
handin4.py 

This module contains functions for reading word lists from files, 
performing word list comparisons using linear search and binary 
search and using dictionaries for word lookup

Functions:
- wordfile_to_list(filename)
- wordfile_differences_linear_search(file1, file2)
- binary_search(sorted_list, element)
- wordfile_differences_binary_search(file1, file2)
- wordfile_to_dict(filename)
- wordfile_differences_dict_search(file1, file2)

"""

def wordfile_to_list(filename):
    """
    Reads a file and returns a list of words (as strings)
    
    Args:
    filename (str): name of file
    
    Returns:
    wordlist: list of words
    """
    file = open(filename, 'r')
    wordlist = []
    for line in file:
        # remove newline characters
        line = line.strip()  
        wordlist.append(line)
    file.close
    return wordlist


def wordfile_differences_linear_search(file1, file2):
    """
    Compares two word lists and returns words that are in 
    the first list but not in the second list using linear search

    Args:
    file1 (str): filename for first word list
    file2 (str): filename for second word list

    Returns:
    differences: list of words that are in file1 but not in file2 
    (case sensitive)
    """
    wordlist1 = wordfile_to_list(file1)
    wordlist2 = wordfile_to_list(file2)
    
    differences = []
    
    for word1 in wordlist1:
        if word1 not in wordlist2:
            differences.append(word1)
    
    return differences


def binary_search(sorted_list, element):
    """
    Search for an element in a sorted list using binary search

    Args:
    sorted_list (list): sorted list to search
    element: element to search

    Returns:
    boolen: true if element is found, false otherwise
    """
    index_start = 0
    index_end = len(sorted_list)
    while (index_end - index_start) > 0:
        index_current = (index_end - index_start) // 2 + index_start
        if element == sorted_list[index_current]:
            return True
        elif element < sorted_list[index_current]:
            index_end = index_current
        elif element > sorted_list[index_current]:
            index_start = index_current + 1
    return False


def wordfile_differences_binary_search(file1, file2):
    """
    Compares two word files using binary search and 
    returns words present in file1 but not in file2

    Args:
    file1 (str): filename for first word list
    file2 (str): filename for second word list

    Returns:
    differences: list of words in file1 but not in file2
    """
    # read word lists from the input files and sort them
    wordlist1 = wordfile_to_list(file1)
    wordlist2 = wordfile_to_list(file2)
    # sort the second list for binary search
    wordlist2.sort()  
    
    # list to store the differences
    differences = []
    
    # binary search for each word in wordlist1
    for word1 in wordlist1:
        if not binary_search(wordlist2, word1):
            differences.append(word1)
    
    return differences


def wordfile_to_dict(filename):
    """
    Reads a file and returns a dictionary 
    with words as keys and None as values
    
    Args:
    filename (str): name of the file
    
    Returns:
    wird_dict: dictionary with words as keys and None as values
    """
    word_dict = {}
    file = open(filename, 'r')
    for line in file:
        # remove trailing newline characters
        word = line.strip()
        word_dict[word] = None
    file.close
    return word_dict


def wordfile_differences_dict_search(file1, file2):
    """
    Compares two word files using dictionary search and 
    returns words present in file1 but not in file2

    Args:
    file1 (str): name of the first file
    file2 (str): name of the second file

    Returns:
    differences: list of words in file1 but not in file2
    """
    # read word list from the first file and create a dictionary from the second file
    wordlist1 = wordfile_to_list(file1)
    worddict2 = wordfile_to_dict(file2)
    
    # list to store the differences
    differences = []
    
    # dictionary search for each word in wordlist1
    for word1 in wordlist1:
        if word1 not in worddict2:
            differences.append(word1)
    
    return differences
