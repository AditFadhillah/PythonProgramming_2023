import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches
from handin5_project import ColorMapper
from handin5_project import construct_rectangles
from handin5_project import plot_stripes

filename = 'Land_and_Ocean_summary.txt'

# use numpy.genfromtxt to read the data, specify the delimiter
anomaly_data = np.genfromtxt(filename, delimiter='     ', comments='%', skip_header=4)

# extract year values (first column) and anomaly values
years = anomaly_data[:, 0]
anomalies = anomaly_data[:, 1]

# access the year and anomaly values
print("Year values:", years)
print("Anomaly values:", anomalies)

# new ColorMapper object using anomalies
color_mapper = ColorMapper(anomalies)

# call the get_color() method
color = color_mapper.get_color(0.0)  # Should correspond to white
print("Color for zero anomaly:", color)

# sample data for testing
""" years = [2000, 2001, 2002, 2003]
anomalies = [0.2, -0.1, 0.5, -0.3] """

# construct rectangles
rectangles = construct_rectangles(years, anomalies)

# create a ColorMapper
color_mapper = ColorMapper(anomalies)

# visualize the stripes using plot_stripes function
plot_stripes(rectangles, color_mapper)

