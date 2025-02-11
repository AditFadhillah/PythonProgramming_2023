def read_matrix():
    matrix = []
    while True:
        row_input = input("Enter a row of numbers separated by spaces (or press Enter to finish): ")
        if not row_input:
            break
        row = [int(num) for num in row_input.split()]
        matrix.append(row)
    return matrix

def scalar_multiplication(matrix, scalar):
    result = [[element * scalar for element in row] for row in matrix]
    return result

def transpose(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result

if __name__ == "__main__":
    print("Please input your matrix below:")
    original_matrix = read_matrix()
    print("\nYour matrix:")
    for row in original_matrix:
        print(row)

    scalar = 8
    scaled_matrix = scalar_multiplication(original_matrix, scalar)
    print("\nScalar multiplication with 8:")
    for row in scaled_matrix:
        print(row)

    transposed_matrix = transpose(original_matrix)
    print("\nTransposition:")
    for row in transposed_matrix:
        print(row)
