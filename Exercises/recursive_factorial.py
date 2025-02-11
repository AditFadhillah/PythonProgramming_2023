def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        user_input = int(input("Non-negative integer: "))
        if user_input < 0:
            print("Please enter a non-negative integer.")
        else:
            result = factorial(user_input)
            print(result)
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
