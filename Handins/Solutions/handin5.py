"""Handin 5"""

import random
import numpy as np

def count_larger_than_neighbor_without_loops(list_of_numbers):
    """Find elements in array that are larger than their left neighbor."""
    array_of_numbers = np.array(list_of_numbers)
    return np.sum(array_of_numbers[1:] > array_of_numbers[:-1])

def read_mnist_csv(filename):
    """Read MNIST CSV data into a numpy array"""
    return np.genfromtxt(filename, delimiter=',', skip_header=1)

def group_by_label(data):
    """Group entries in data by their label value"""
    group_list = []
    for i in range(10):
        group_list.append(data[np.where(data[:, 0] == i)])
    return group_list

def get_image(digit_image_groups, digit):
    """Return single image from group list - reshaped to a 28x28 image"""

    digit_image_group = digit_image_groups[digit] 
    
    random_index = random.randint(0, digit_image_group.shape[0]-1)
    digit_image = digit_image_group[random_index]
    
    return digit_image[1:].reshape([28, 28])
