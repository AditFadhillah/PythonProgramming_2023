"""
handin3.py

This module contains functions for reading and processing word files

"""

import re


def read_word_file(filename):
    """
    Open and read a file line by line and return a list of tuples
    where each tuple contains the line number

    Args:
        filename (str): name of file

    Returns:
        list of tuples with line number and content
    """
    # open file
    file = open(filename, 'r')
    word_list = []
    # iterate over lines
    for line_number, line in enumerate(file):
        line = line.strip()  # remove newline characters
        word_list.append((line_number, line))
    
    # close the file
    file.close 
    return word_list
   

def read_word_file2(filename, filter_re_str=""):
    """
    Open and read a file line by line, filter the lines based on the given regular expression,
    and return a list of tuples where each tuple contains the line number and the content
    
    Args:
        filename (str): the name of the file to be read
        filter_re_str (str): regular expression string for filtering lines (optional)

    Returns:
        list: list of tuples containing line number and matching line content
    """
    # compile regular expression for filtering
    filter_regex = re.compile(filter_re_str)
    # open file 
    file = open(filename, 'r')
    word_list = []
    # iterate over lines
    for line_number, line in enumerate(file):
        line = line.strip()  # remove newline characters
        # cheack if the line matches the filter or there is no filter
        if not filter_re_str or filter_regex.search(line):
            word_list.append((line_number, line))

    # close file
    file.close 
    return word_list
