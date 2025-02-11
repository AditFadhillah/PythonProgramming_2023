'''Handin3 Project Module'''

def read_data2(filename, year_range=(float("-inf"), float("inf"))):
    """Reads tabular data from filename and returns as list of strings. The function 
       assumes that the first value in each line contains a year value. Using the
       year_range argument, a range of values can be specified"""

    # Open file, read contents in as list of strings, and close file again
    f = open('Land_and_Ocean_summary.txt')
    list_of_lines = f.readlines()
    f.close()

    # Create empty list
    data_list = []
    
    # Iterate over strings in list_of_lines 
    for line in list_of_lines:
        
        # Remove whitespace and ends of string, save in new variable 
        line_stripped = line.strip()

        # If line is empty after stripping, or is a comments,
        # continue to next iteration (i.e. next line)
        if len(line_stripped) == 0 or line_stripped[0] == '%':
            continue

        # Split line into a list of small strings (separated by spaces)
        split_line = line_stripped.split(' ')

        # Extract first element, and convert to integer
        year = int(split_line[0])

        # If year is within specified range, add it to data_list
        if year >= year_range[0] and year < year_range[1]:
            data_list.append(line)

    # Return data_list to the caller of the function
    return data_list


def read_data3(filename, year_range=(float("-inf"), float("inf"))):
    """Reads tabular data from filename and returns as dictionary with years as keys. 
       The function assumes that the first value in each line contains a year value. 
       Using the year_range argument, a range of values can be specified"""

    data_dict = {}

    file_handle = open(filename)

    # Note: we can iterate directly over a file object
    for line in file_handle:

        # Overwriting line with stripped version
        # (we don't need original)
        line = line.strip()

        if len(line) == 0 or line[0] == '%':
            continue

        # Split string into list of strings
        line_split = line.split()

        year = int(line_split[0])
        
        # Convert list of strings to a list of floats
        line_split_numbers = []
        for entry in line_split[1:]:   # Note: skipping year value
            line_split_numbers.append(float(entry))

        if year >= year_range[0] and year < year_range[1]:
            data_dict[year] = line_split_numbers
            
    file_handle.close()

    return data_dict
