# create variable
number_str = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20\n"

# use string method '.strip' to remove newline
number_str_cleaned = number_str.strip()

# use string method '.split' to split the string
number_str_list = number_str_cleaned.split()

# use for-loop to print each string
for number in number_str_list:
    print(number)
    