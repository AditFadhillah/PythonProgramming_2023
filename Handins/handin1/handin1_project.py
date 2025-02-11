# open and read the txt file, store each line in variable
with open("Land_and_Ocean_summary.txt", "r") as file:
    list_of_lines = file.readlines()

# iterate the variable
for line in list_of_lines:
    # clean the lines
    line = line.strip()
    # skip line that starts with '%'
    if not line or line.startswith("%"):
        continue
    
    # split the string to be individual lines
    pieces = line.split()

    # print the first entry, for the year larger or equal than 2000
    if int(pieces[0]) >= 2000:
        print(pieces[0])