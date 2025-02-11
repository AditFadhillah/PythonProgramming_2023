f = open('Land_and_Ocean_summary.txt')   # Open file in read mode
list_of_lines = f.readlines()            # Read file into a list of strings
f.close()

for line in list_of_lines:               # Iterate over list of strings

    # Remove white space at beginning and end.
    line_stripped = line.strip()         

    # Skipping empty lines and comment lines
    # Now that we have called strip(), empty lines
    # will have length 0. Otherwise, empty lines
    # have a newline character.
    if len(line_stripped) == 0 or line[0] == '%':
        # Note that continue jumps on to the next iteration,
        # so the following lines are skipped
        continue   

    # Split line into a list of small strings
    split_line = line_stripped.split(' ')
    
    # Choosing first element - and convert to integer
    year = int(split_line[0])

    # Now that year is an integer, we can compare it to 2000
    if year >= 2000:
        print(year)

    
