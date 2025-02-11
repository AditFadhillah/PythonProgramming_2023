import numpy as np
import matplotlib.pyplot as plt

import handin5

# Q1
larger_than_neighbor_count = handin5.count_larger_than_neighbor_without_loops([6,9,4,8,7,1,2])
print(larger_than_neighbor_count)

# Q2
mnist_data = handin5.read_mnist_csv('mnist_test_200.csv')

# Q3
digit_image_groups = handin5.group_by_label(mnist_data)

# Q4
digit_image = handin5.get_image(digit_image_groups, digit=0)
plt.imshow(digit_image, cmap='gray')
plt.axis('off')
plt.savefig('random_image.png')
