def fibonacci(n):
    a, b = 1, 1
    for x in range(n):
        print(a)
        a, b = b, a + b

if __name__ == "__main__":
    user_input = input("Number of Fibonacci Sequence numbers: ")
    if (user_input.isdigit()) and (int(user_input) >= 0):
        user_input = int(user_input)
        fibonacci(user_input)
    else:
        print("Please input a non-negative integer.")
