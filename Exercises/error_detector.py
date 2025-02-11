user_input = input("Your input number:")

if user_input.isdigit():
    number = int(user_input)
    if number % 2 == 0:
        print("OK!")
    else:
        print("Error detected!")
else:
    print("Please input a digit.")
    