def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        currval = numbers[i]
        pos = i

        while pos > 0 and numbers[pos - 1] > currval:
            numbers[pos] = numbers[pos - 1]
            pos = pos - 1
        
        numbers[pos] = currval
    print(numbers)

if __name__ == "__main__":
    user_input = input("Input your numbers: ")
    input_list = user_input.split()

    if all(num.isdigit() for num in input_list):
        numbers = [int(num) for num in input_list]
        insertion_sort(numbers)
    else:
        print("Please input only numbers!")
