minimum = None
maximum = None

while True:
    user_input = input("Input: ")

    if user_input.isdigit():
        num = int(user_input)

        if maximum is None or num > maximum:
            maximum = num
            
        if minimum is None or num < minimum:
            minimum = num
    else:
        break

if maximum is not None or minimum is not None:
    print("Maximum:", maximum)
    print("Minimum:", minimum) 
else:
    print("No integer given.")
