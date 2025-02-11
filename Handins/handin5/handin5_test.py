import matplotlib.pyplot as plt
from handin5 import count_larger_than_neighbor_without_loops
from handin5 import read_mnist_csv
from handin5 import group_by_label
from handin5 import get_image


# test count_larger_than_neighbor_without_loops function
list_of_numbers = [6,9,4,8,7,1,2,1]
larger_than_neigbor_count = count_larger_than_neighbor_without_loops(list_of_numbers)

print("Count of elements larger than their left neighbor:", larger_than_neigbor_count)


# test read_mnist_csv funtion
mnist_data = read_mnist_csv('mnist_test_200.csv')

print("Shape of mnist_data:", mnist_data)

# test group_by_label function
digit_image_groups = group_by_label(mnist_data)

for digit, group in enumerate(digit_image_groups):
    print(f"Digit {digit}: {group.shape[0]} images")

# test get_image function
selected_digit = 3
digit_image = get_image(digit_image_groups, selected_digit)

# show the randomly selected image
plt.imshow(digit_image, cmap='gray')
plt.title(f"Random image of digit {selected_digit}")
plt.axis('off')
plt.savefig('random_image.png')
plt.show()

