"""
handin5.py

This module provides functions for analyzing and manipulating MNIST dataset. 
Includes functions for working with MNIST CSV files. 

Functions:
- count_larger_than_neighbor_without_loop(list_of_numbers)
- read_mnist_csv(filename)
- group_by_label(mnist_data)
- get_image(digit_image_groups, digit)

"""
import numpy as np

def count_larger_than_neighbor_without_loops(list_of_numbers):
    """
    Count the elements in a list that are larger than the left neighbors

    Args:
    list_of_numbers (list)

    Returns:
    count (int): the count of elements larger than the left neighbors
    """
    arr = np.array(list_of_numbers)

    curr_elem = arr[1:]
    left_neighbor_elem = arr[:-1]

    count = np.sum(curr_elem > left_neighbor_elem)

    return count

def read_mnist_csv(filename):
    """
    Read and parse data from a MNIST CSV file

    Args:
    filename (str): MNIST CSV filename

    Returns:
    mnist_data (np.array): numpy array with the parsed data
    """
    mnist_data = np.genfromtxt(filename, delimiter=',', skip_header=1)

    return mnist_data

def group_by_label(mnist_data):
    """
    Group MNIST data by digit labels

    Args:
    mnist_data (np.array): numpy array with MNIST data

    Returns:
    digit_image_groups (list): list of numpy arrays, 
    each with data for a specific digit
    """
    digit_image_groups = []

    for digit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        digit_data = mnist_data[mnist_data[:, 0] == digit]
        digit_image_groups.append(digit_data)

    return digit_image_groups

def get_image(digit_image_groups, digit):
    """
    Get a random image of a specified digit from a list of digit image groups

    Args:
    digit_image_groups (list): list of numpy arrays
    digit (int): the digit the image is requested (0 to 9)

    Returns:
    random_image (np.array): a random 28x28 image of the selected digit
    
    Raises:
    ValueError: if the 'digit' argument is not in the range of 0 to 9.
    """
    if digit < 0 or digit > 9:
        raise ValueError("Digit argument should from 0 to 9") 
    
    digit_group = digit_image_groups[digit]

    num_images = digit_group.shape[0]

    random_index = np.random.randint(0, num_images)

    random_image = digit_group[random_index, 1:]

    random_image = random_image.reshape(28, 28)

    return random_image

