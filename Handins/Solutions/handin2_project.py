# Open file, read contents in as list of strings, and close file again
file_handle = open('Land_and_Ocean_summary.txt')
list_of_lines = file_handle.readlines()
file_handle.close()

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

    # Add line to list (not that this is the original line)
    data_list.append(line)


def read_data(filename):
    """Reads tabular data from filename and returns as list of strings"""

    # Open file, read contents in as list of strings, and close file again
    file_handle = open('Land_and_Ocean_summary.txt')
    list_of_lines = file_handle.readlines()
    file_handle.close()

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

        # Add line to list (not that this is the original line)
        data_list.append(line)

    # Return data_list to the caller of the function
    return data_list



    
