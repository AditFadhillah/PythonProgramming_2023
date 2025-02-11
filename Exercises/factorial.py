def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    print(result)

if __name__ == "__main__":
    user_input = input("Non-negative integer: ")
    if (user_input.isdigit()) and (int(user_input) >= 0):
        user_input = int(user_input)
        factorial(user_input)
    else:
        print("Please input a non-negative integer.")
