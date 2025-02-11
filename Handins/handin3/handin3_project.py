"""
handin3_project.py

This module contains functions for reading and processing data files

"""

def read_data(filename):
    """
    Function to read from file and return as list of strings

    Args: 
        filename (str)

    Return:
        list of strings
    
    """

    text = open(filename, "r")
    data_list = []

    # iterate each line
    for line in text:
        # remove leading and trailing whitespace
        line = line.strip() 
        # skip empty lines and lines starts with "%"
        if not line or line.startswith("%"): 
            continue
        
        # add to data_list
        data_list.append(line) 
    text.close

    # return the list of strings
    return data_list 


def read_data2(filename, year_range=None):
    """
    Function to read from file, filter by years, and return list of strings

    Args: 
        filename (str), year_range (int) (optinal)

    Return:
        list of strings
    
    """

    text = open(filename, "r")
    data_list = []

    # iterate
    for line in text:
        line = line.strip()
        if not line or line.startswith("%"):
            continue
        
        # split the line into year and value
        year_str, *data = line.split()
        # convert to int
        year = int(year_str)
        
        # check if year is in the year range
        if year_range is None or (year_range[0] <= year < year_range[1]):
            # add to data_list
            data_list.append(line) 
    
    text.close()
    return data_list


def read_data3(filename, year_range=None):
    """
    Function to read from file, filter by years, and return as dictionary

    Args: 
        filename (str) year_range (int) (optinal)

    Return:
        dictionary
    
    """
    text = open(filename, "r")
    data_dict = {}

    # iterate
    for line in text:
        line = line.strip()
        if not line or line.startswith("%"):
            continue
        
        # split the line into year and value
        year_str, *data_values = line.split()
        # convert to int
        year = int(year_str)

        # check if year is in the year range
        if year_range is None or (year_range[0] <= year < year_range[1]):
            # convert values to floats, handling "NaN" as "nan"
            data_list = []
            for val in data_values:
                if val != "NaN":
                    data_list.append(float(val))
                else:
                    data_list.append(float("nan"))
            
            data_dict[year] = data_list
    
    text.close()
    # return dictionary of data
    return data_dict 
