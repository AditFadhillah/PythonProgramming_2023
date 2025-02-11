
user_input = input("Please give your grade in percentages (0-100): ")

if user_input.isdigit() and 0 <= int(user_input) <= 100:
    percent_grade = int(user_input)
    if percent_grade >= 90:
        letter_grade = "A"
    elif percent_grade >= 80:
        letter_grade = "B"
    elif percent_grade >= 70:
        letter_grade = "C"
    elif percent_grade >= 65:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print("Your letter grade is", letter_grade)
else:
    print("Please input a digit between 0 and 100.")
