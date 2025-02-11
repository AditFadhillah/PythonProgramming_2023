import math

def calculate_standard_deviation(numbers):
    if len(numbers) < 2:
        return 0.0

    # Calculate the mean (average)
    mean = sum(numbers) / len(numbers)

    # Calculate the sum of squared differences
    squared_differences = [(x - mean) ** 2 for x in numbers]

    # Calculate the variance
    variance = sum(squared_differences) / len(numbers)

    # Calculate the standard deviation
    std_deviation = math.sqrt(variance)

    return std_deviation

def main():
    numbers = []

    while True:
        user_input = input("Input: ")
        
        if user_input.lower() == "stop":
            break

        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            break

    if numbers:
        minimum = min(numbers)
        maximum = max(numbers)
        average = sum(numbers) / len(numbers)
        std_deviation = calculate_standard_deviation(numbers)

        print(f"Minimum: {minimum}")
        print(f"Maximum: {maximum}")
        print(f"Average: {average:.1f}")
        print(f"SD: {std_deviation:.16f}")
    else:
        print("No valid input provided.")

if __name__ == "__main__":
    main()
