'''Handin3 Module'''

import re


def read_word_file(filename):
    # Read file containing words, and return a list of (line-number, line) values
    
    file_handle = open(filename)
    input_lines = file_handle.readlines()
    file_handle.close()
    
    line_list = []
    # Remember, enumerate will provide both
    # the index of the list and its value
    for index, line in enumerate(input_lines):

        # Overwrite existing line variable with stripped version
        # (we don't need the original anymore)
        line = line.strip()

        line_list.append((index, line))
            
    return line_list

    
def read_word_file2(filename, filter_re_str=""):
    """Read file containing words, and return a list of (line-number, line) values.
       A filter_re_str argument can be specified to select for a subset of strings. It
       should be given as a regular expression string."""

    file_handle = open(filename)
    input_lines = file_handle.readlines()
    file_handle.close()

    filter_re = re.compile(filter_re_str)
    
    line_list = []
    # Remember, enumerate will provide both
    # the index of the list and its value
    for index, line in enumerate(input_lines):

        # Overwrite existing line variable with stripped version
        # (we don't need the original anymore)
        line = line.strip()

        # Use regular expression to search for match in line
        match = filter_re.search(line)

        if match:
            line_list.append((index,line))

    return line_list
