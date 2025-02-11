from datetime import datetime

# Prompt the user for their birthday
user_input = input("What is your birthday? (YYYY-MM-DD): ")

try:
    # Parse the input string as a date
    date = datetime.strptime(user_input, "%Y-%m-%d")
    
    # Get the day of the week and print its full name
    day_name = date.strftime("%A")
    
    print(day_name)
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")
