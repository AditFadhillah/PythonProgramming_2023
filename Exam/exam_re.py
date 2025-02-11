

def print_lines(filename):
    """Printing lines one by one"""
    with open(filename) as input:
        for line in input:
            line = line.strip()
            print(line)

def order_numbers(filename):
    """printing numbers in order"""
    numbers = []
    with open(filename) as input:
        for line in input:
            line = line.strip()
            split_line = line.split()
            numbers.append(int(split_line[-1]))

    numbers.sort()
    for number in numbers:
        print(number)

def order_lines(filename):
    """printing numbers in order"""
    entries = []
    with open(filename) as input:
        for line in input:
            line = line.strip()
            split_line = line.split()
            entries.append((int(split_line[-1]), line))

    entries.sort()
    print(entries)
    for item in entries:
        print(item[1])

def order_lines_compact(filename):
    """printing numbers in order"""
    with open(filename) as input:
        print("".join([line[1] for line in sorted([(int(line.strip().split()[-1]), line) for line in input])]))


def read_zipcode_file(filename):
    """Read in zipcode file"""
    data = {}
    with open(filename) as input:
        header = input.readline().strip().split(',')

        for line in input:
            line = line.strip()

            if len(line) == 0:
                continue

            split_line = line.split(',')

            row_dict = {}
            for i, entry in enumerate(split_line):
                row_dict[header[i]] = entry

            zipcode = row_dict['zipcode']
            if zipcode not in data:
                data[zipcode] = row_dict
    return data

def count_zipcodes_per_state(zipcode_dict, state):
    """Counting how many zip codes exist for a given state"""
    zipcodes = {}
    for entry in zipcode_dict.values():
        if entry['state'] == state:
            zipcodes[entry['zipcode']] = True
    return len(zipcodes)

def lon_lat_distance(lon1, lat1, lon2, lat2, radius=6373):
    """Calculate distance (in km) between two (longitude, latitude) pairs"""
    import math
    theta1 = lon1*math.pi/180.   # Convert to radians
    theta2 = lon2*math.pi/180.
    phi1 = (90.-lat1)*math.pi/180.  # Subtract from 90 to get spherical coordinates
    phi2 = (90.-lat2)*math.pi/180.
    arc_len = math.acos(min(1.,math.sin(phi1)*math.sin(phi2)*math.cos(theta2-theta1)+math.cos(phi1)*math.cos(phi2)))
    return arc_len * radius

def max_distance(zipcode_dict):
    """find zipcode pair with max distance between them"""

    distances = []
    for entry1 in zipcode_dict.values():
        lat1 = float(entry1['latitude'])
        lon1 = float(entry1['longitude'])
        for entry2 in zipcode_dict.values():
            lat2 = float(entry2['latitude'])
            lon2 = float(entry2['longitude'])
            distance = lon_lat_distance(lon1, lat1, lon2, lat2)
            distances.append((distance, entry1['zipcode'], entry2['zipcode']))
    distances.sort()
    return distances[-1]

import re
happy_sad_re = re.compile(r'[:;][-o]?[)(]')
happy_sad_re2 = re.compile(r'([:;][-o]?)([)(])')

def find_happy(input_text):
    """Print only happy emoticons"""
    for match in happy_sad_re2.finditer(input_text):
        if match.group(2) == ")":
            print(match.group(0))

def make_string_happy(input_text):
    """Return string where all sad emoticons have been replaced by equivalent happy ones"""
    return happy_sad_re2.sub(r"\1)", input_text)

import numpy as np

def read_image_array(filename):
    """Read image array from file"""
    data = np.loadtxt(filename, dtype=str, comments=None, delimiter=',')
    return data

def change_image_array_foreground(image_array, foreground_char):
    """Change foreground character in image array"""

    image_array_copy = image_array.copy()
    image_array_copy[image_array == '#'] = foreground_char
    return image_array_copy

def frame_image_array(image_array, frame_width):
    """Add frame to image array"""
    image_array_framed = np.full((image_array.shape[0]+(2*frame_width), image_array.shape[1]+(2*frame_width)), "#", dtype=str)
    image_array_framed[frame_width:-frame_width, frame_width:-frame_width] = image_array
    return image_array_framed

def make_image_array_happy(image_array, label_array):
    """Modify image array so that it becomes a happy face"""
    #print(label_array)
    image_array_copy = image_array.copy()
    image_array_copy[label_array == "MOUTH_LOWER"] = ' '
    image_array_copy[label_array == "MOUTH_UPPER"] = '#'
    return image_array_copy

import pandas as pd

def mnist_pretty_print(mnist_image_array):
    """Return a nicer string representation of a binary MNIST image"""
    return np.array2string(mnist_image_array, separator=' ',
                           formatter={'int_kind': lambda x: ' ' if x==0 else '#'})

class MnistCollection:
    """Class to represent mnist images"""

    def __init__(self, filename):
        """contructor"""
        self.data = (pd.DataFrame(np.genfromtxt(filename,
                                                skip_header=1,
                                                delimiter=',')).astype(int).set_index(0) > (255 / 2)).astype(int)
    def get_images_for_digit(self, digit):
        """Retrieve images for specific digit"""
        #mask = self.data[:,0] == digit
        grps = list(self.data.groupby(self.data.index))
        assert grps[digit][0] == digit
        return grps[digit][1].values.reshape(-1, 28,28)

    def get_slimmest_image_for_digit(self, digit):
        """Retrieve thinnest image of digit"""
        images = self.get_images_for_digit(digit)
        return images[np.argmin(np.sum(images.reshape(-1, 28*28), axis=-1))]
